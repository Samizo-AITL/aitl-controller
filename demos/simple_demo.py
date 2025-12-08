import os
import numpy as np
import matplotlib.pyplot as plt

# =========================
#  First-order Plant Model
# =========================
class Plant:
    def __init__(self, tau=1.0):
        self.x = 0.0
        self.tau = tau

    def step(self, u, dt=0.01):
        dx = (-self.x + u) / self.tau
        self.x += dx * dt
        return self.x


# =========================
#  PID Controller (Inner Loop)
# =========================
class PID:
    def __init__(self, kp, ki, kd):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.i = 0.0
        self.prev_e = 0.0

    def __call__(self, e, dt=0.01):
        self.i += e * dt
        d = (e - self.prev_e) / dt
        self.prev_e = e
        return self.kp * e + self.ki * self.i + self.kd * d


# =========================
#  FSM (Middle Layer)
# =========================
class FSM:
    def __init__(self):
        self.state = "NORMAL"

    def transition(self, e):
        if abs(e) > 1.0:
            self.state = "DISTURB"
        elif self.state == "DISTURB" and abs(e) < 0.2:
            self.state = "TUNE"
        elif self.state == "TUNE" and abs(e) < 0.05:
            self.state = "NORMAL"
        return self.state


# =========================
#  LLM Layer (Gain Tuning)
# =========================
class FakeLLM:
    def tune(self, pid, e):
        # Increase gains when error is large
        if abs(e) > 0.5:
            pid.kp *= 1.02
            pid.kd *= 1.01
        # Decrease gains when system stabilizes
        else:
            pid.kp *= 0.995
            pid.kd *= 0.99


# =========================
#  Integrated AITL Controller
# =========================
class AITL:
    def __init__(self, pid, fsm, llm):
        self.pid = pid
        self.fsm = fsm
        self.llm = llm

    def step(self, r, x, dt=0.01):
        e = r - x
        state = self.fsm.transition(e)

        # LLM tuning phase
        if state == "TUNE":
            self.llm.tune(self.pid, e)

        u = self.pid(e, dt)
        return u, state


# =========================
#  Simulation
# =========================
def main():
    dt = 0.01
    T = 10.0

    plant = Plant()
    pid = PID(1.0, 0.2, 0.01)
    fsm = FSM()
    llm = FakeLLM()
    ctl = AITL(pid, fsm, llm)

    time = []
    x_log, u_log, state_log = [], [], []

    for t in np.arange(0, T, dt):
        r = 1.0
        x = plant.x
        u, state = ctl.step(r, x, dt)
        plant.step(u, dt)

        time.append(t)
        x_log.append(x)
        u_log.append(u)
        state_log.append(state)

    # =========================
    # Plot
    # =========================
    fig, ax1 = plt.subplots()

    ax1.plot(time, x_log, label="Plant output x")
    ax1.plot(time, [1.0] * len(time), "--", label="Reference", alpha=0.7)
    ax1.set_xlabel("Time [s]")
    ax1.set_ylabel("x")
    ax1.legend()
    ax1.grid(True)

    # FSM visualization
    ax2 = ax1.twinx()
    fsm_num = {"NORMAL": 0, "DISTURB": 1, "TUNE": 2}
    ax2.plot(time, [fsm_num[s] for s in state_log], label="FSM State", alpha=0.3)
    ax2.set_ylabel("FSM State (0=NORMAL, 1=DISTURB, 2=TUNE)")

    plt.title("AITL Controller Demo (PID × FSM × LLM)")
    plt.tight_layout()

    # =========================
    # Save PNG into assets/plot
    # =========================
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    save_dir = os.path.join(BASE_DIR, "assets", "plot")
    os.makedirs(save_dir, exist_ok=True)

    save_path = os.path.join(save_dir, "simple_demo.png")
    plt.savefig(save_path, dpi=200)
    print(f"Saved PNG to: {save_path}")

    plt.show()


if __name__ == "__main__":
    main()

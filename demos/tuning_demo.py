import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# =========================
# Add src/ to PYTHONPATH
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, "src")
sys.path.append(SRC_DIR)

# Import AITL controller modules
from aitl_controller.plant import Plant
from aitl_controller.pid import PID
from aitl_controller.fsm import FSM
from aitl_controller.llm import FakeLLM
from aitl_controller.controller import AITL


# =========================
# Main simulation (Tuning Demo)
# =========================
def main():
    dt = 0.01
    T = 12.0

    # Initial gains intentionally weak to show LLM adaptation
    plant = Plant()
    pid = PID(0.8, 0.1, 0.01)
    fsm = FSM()
    llm = FakeLLM()
    ctl = AITL(pid, fsm, llm)

    time = []
    x_log, u_log = [], []
    kp_log, kd_log = [], []
    state_log = []

    # Simulation loop
    for t in np.arange(0, T, dt):
        r = 1.0
        x = plant.x

        # AITL control step
        u, state = ctl.step(r, x, dt)
        plant.step(u, dt)

        # Logging
        time.append(t)
        x_log.append(x)
        u_log.append(u)
        kp_log.append(pid.kp)
        kd_log.append(pid.kd)
        state_log.append(state)

    # =========================
    # Plotting
    # =========================
    fig, axs = plt.subplots(3, 1, figsize=(8, 8), sharex=True)

    # Output tracking
    axs[0].plot(time, x_log, label="Plant Output x")
    axs[0].plot(time, [1.0] * len(time), "--", label="Reference")
    axs[0].set_ylabel("x")
    axs[0].legend()
    axs[0].grid(True)

    # PID Gain Adaptation
    axs[1].plot(time, kp_log, label="Kp")
    axs[1].plot(time, kd_log, label="Kd")
    axs[1].set_ylabel("PID Gains")
    axs[1].legend()
    axs[1].grid(True)

    # FSM state transitions
    state_int = [{"NORMAL": 0, "DISTURB": 1, "TUNE": 2}[s] for s in state_log]
    axs[2].plot(time, state_int, ".", alpha=0.3)
    axs[2].set_ylabel("FSM State")
    axs[2].set_xlabel("Time [s]")
    axs[2].grid(True)

    plt.suptitle("AITL Tuning Demo (LLM-based PID Gain Adaptation)")
    plt.tight_layout()

    # =========================
    # Save PNG into assets/plot
    # =========================
    save_dir = os.path.join(BASE_DIR, "assets", "plot")
    os.makedirs(save_dir, exist_ok=True)

    save_path = os.path.join(save_dir, "tuning_demo.png")
    plt.savefig(save_path, dpi=200)
    print(f"Saved PNG to: {save_path}")

    plt.show()


if __name__ == "__main__":
    main()

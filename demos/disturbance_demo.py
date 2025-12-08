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

# Import modules from aitl_controller package
from aitl_controller.plant import Plant
from aitl_controller.pid import PID
from aitl_controller.fsm import FSM
from aitl_controller.llm import FakeLLM
from aitl_controller.controller import AITL


# =========================
# Disturbance model
# =========================
def disturbance(t: float) -> float:
    """
    Simple disturbance model.
    Applies a constant disturbance between t = 3 and 6 seconds.
    Modify freely if you want different waveforms.
    """
    if 3.0 <= t < 6.0:
        return 0.8
    return 0.0


# =========================
# Main simulation
# =========================
def main():
    dt = 0.01       # simulation time-step
    T = 10.0       # total time [s]

    # Controllers and plant
    plant = Plant()
    pid = PID(1.0, 0.2, 0.01)
    fsm = FSM()
    llm = FakeLLM()
    ctl = AITL(pid, fsm, llm)

    time = []
    x_log, u_log, d_log, state_log = [], [], [], []

    for t in np.arange(0, T, dt):
        r = 1.0          # reference
        x = plant.x      # current plant output

        # AITL controller (PID × FSM × LLM)
        u, state = ctl.step(r, x, dt)

        # External disturbance input
        d = disturbance(t)

        # Apply control + disturbance to plant
        plant.step(u + d, dt)

        # Logging
        time.append(t)
        x_log.append(x)
        u_log.append(u)
        d_log.append(d)
        state_log.append(state)

    # =========================
    # Plotting
    # =========================
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

    # Plant output
    ax1.plot(time, x_log, label="Plant output x")
    ax1.plot(time, [1.0] * len(time), "--", label="Reference", alpha=0.7)
    ax1.set_ylabel("x")
    ax1.legend()
    ax1.grid(True)

    # Control input, disturbance, and FSM
    ax2.plot(time, u_log, label="Control u")
    ax2.plot(time, d_log, label="Disturbance d")

    state_int = [ {"NORMAL": 0, "DISTURB": 1, "TUNE": 2}[s] for s in state_log ]
    ax2.plot(time, state_int, ".", alpha=0.3, label="FSM State (0=N,1=D,2=T)")

    ax2.set_xlabel("Time [s]")
    ax2.set_ylabel("u, d, state")
    ax2.legend()
    ax2.grid(True)

    plt.suptitle("AITL Disturbance Demo (PID × FSM × LLM)")
    plt.tight_layout()

    # =========================
    # Save PNG into assets/plot
    # =========================
    save_dir = os.path.join(BASE_DIR, "assets", "plot")
    os.makedirs(save_dir, exist_ok=True)

    save_path = os.path.join(save_dir, "disturbance_demo.png")
    plt.savefig(save_path, dpi=200)
    print(f"Saved PNG to: {save_path}")

    plt.show()


if __name__ == "__main__":
    main()

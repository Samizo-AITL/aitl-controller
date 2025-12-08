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
# Reference signal definition
# =========================
def reference(t: float) -> float:
    """
    Dynamic reference signal r(t):

    - 0–3 s:  constant value 1.0
    - 3–6 s:  step down to 0.5
    - 6–10 s: sinusoidal tracking target

        r(t) = 1.0 + 0.3 sin(2π·0.5·(t − 6))

    Modify freely if additional patterns needed.
    """
    if t < 3.0:
        return 1.0
    elif t < 6.0:
        return 0.5
    else:
        return 1.0 + 0.3 * np.sin(2 * np.pi * 0.5 * (t - 6))


# =========================
# Main simulation
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
    r_log, x_log, u_log, state_log = [], [], [], []

    # Simulation loop
    for t in np.arange(0, T, dt):
        r = reference(t)
        x = plant.x

        # AITL control (PID × FSM × LLM)
        u, state = ctl.step(r, x, dt)

        # Plant update
        plant.step(u, dt)

        # Logging
        time.append(t)
        r_log.append(r)
        x_log.append(x)
        u_log.append(u)
        state_log.append(state)

    # =========================
    # Plotting
    # =========================
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

    # Plant output vs reference
    ax1.plot(time, x_log, label="Plant output x")
    ax1.plot(time, r_log, "--", label="Reference r(t)", alpha=0.8)
    ax1.set_ylabel("x")
    ax1.legend()
    ax1.grid(True)

    # Control input & FSM state
    ax2.plot(time, u_log, label="Control input u")

    state_int = [ {"NORMAL": 0, "DISTURB": 1, "TUNE": 2}[s] for s in state_log ]
    ax2.plot(time, state_int, ".", alpha=0.3, label="FSM State")

    ax2.set_xlabel("Time [s]")
    ax2.set_ylabel("u / FSM")
    ax2.legend()
    ax2.grid(True)

    plt.suptitle("AITL Tracking Demo (PID × FSM × LLM)")
    plt.tight_layout()

    # =========================
    # Save PNG into assets/plot
    # =========================
    save_dir = os.path.join(BASE_DIR, "assets", "plot")
    os.makedirs(save_dir, exist_ok=True)

    save_path = os.path.join(save_dir, "tracking_demo.png")
    plt.savefig(save_path, dpi=200)
    print(f"Saved PNG to: {save_path}")

    plt.show()


if __name__ == "__main__":
    main()

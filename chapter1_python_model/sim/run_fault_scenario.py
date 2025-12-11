import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

from src.pid import PID
from src.aitl_controller import AITLControllerA
from src.llm_placeholder import LLMAdaptiveLayer


def simulate_fault():
    dt = 0.01
    pid = PID(1.0, 0.2, 0.05, dt)
    ctrl = AITLControllerA(pid, LLMAdaptiveLayer())
    ctrl.setpoint = 1.0

    x = 0
    xs, us, states = [], [], []

    for t in range(300):
        if t == 10:
            ctrl.start_cmd = True
        if t == 30:
            ctrl.startup_done = True
        if t == 120:
            ctrl.error_detected = True
        if t == 200:
            ctrl.reset_cmd = True

        u = ctrl.step(x)
        x += u * dt

        xs.append(x)
        us.append(u)
        states.append(ctrl.state.value)

    # ====== Plot ======
    fig, ax1 = plt.subplots()
    ax1.plot(xs, "b-", label="x(t)")
    ax1.set_ylabel("x(t)", color="b")

    ax2 = ax1.twinx()
    ax2.plot(states, "r--", label="state")
    ax2.set_ylabel("state", color="r")

    plt.title("AITL Fault Scenario")

    # ====== Save ======
    os.makedirs("plots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"plots/fault_scenario_{timestamp}.png"
    plt.savefig(filename, dpi=200)

    print(f"[INFO] Saved plot to: {filename}")

    plt.show()


if __name__ == "__main__":
    simulate_fault()

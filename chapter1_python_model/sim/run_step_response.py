import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

from src.pid import PID
from src.aitl_controller import AITLControllerA
from src.llm_placeholder import LLMAdaptiveLayer


def simulate():
    dt = 0.01
    T = 5.0
    N = int(T / dt)

    pid = PID(1.0, 0.2, 0.05, dt)
    ctrl = AITLControllerA(pid, LLMAdaptiveLayer())
    ctrl.setpoint = 1.0

    ctrl.start_cmd = True
    ctrl.startup_done = True

    x = 0
    xs, us = [], []

    for _ in range(N):
        u = ctrl.step(x)
        x += u * dt  # simple plant model

        xs.append(x)
        us.append(u)

    # ====== Plot ======
    plt.figure()
    plt.plot(xs, label="x(t)")
    plt.plot(us, label="u(t)")
    plt.legend()
    plt.title("AITL Step Response")

    # ====== Save ======
    os.makedirs("plots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"plots/step_response_{timestamp}.png"
    plt.savefig(filename, dpi=200)

    print(f"[INFO] Saved plot to: {filename}")

    plt.show()


if __name__ == "__main__":
    simulate()

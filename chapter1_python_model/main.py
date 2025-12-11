from src.pid import PID
from src.llm_placeholder import LLMAdaptiveLayer
from src.aitl_controller import AITLControllerA


def main():
    pid = PID(kp=1.2, ki=0.5, kd=0.1, dt=0.01)
    llm = LLMAdaptiveLayer()
    ctrl = AITLControllerA(pid, llm)

    ctrl.setpoint = 10.0

    x = 0
    for t in range(100):
        if t == 10:
            ctrl.start_cmd = True
        if t == 20:
            ctrl.startup_done = True

        u = ctrl.step(x)
        x += 0.05 * u

        print(f"t={t:03d} state={ctrl.state.name} x={x:.2f} u={u:.2f}")


if __name__ == "__main__":
    main()

from .fsm import AITLState

class AITLControllerA:
    def __init__(self, pid, llm=None):
        self.pid = pid
        self.llm = llm
        self.state = AITLState.IDLE

        # external signals
        self.start_cmd = False
        self.reset_cmd = False
       	self.error_detected = False
        self.startup_done = False

        # control variables
        self.setpoint = 0
        self.measured = 0
        self.control_output = 0

    def _update_fsm(self):
        s = self.state

        if s == AITLState.IDLE:
            if self.start_cmd:
                self.state = AITLState.STARTUP

        elif s == AITLState.STARTUP:
            if self.error_detected:
                self.state = AITLState.FAULT
            elif self.startup_done:
                self.state = AITLState.RUN

        elif s == AITLState.RUN:
            if self.error_detected:
                self.state = AITLState.FAULT

        elif s == AITLState.FAULT:
            if self.reset_cmd:
                self.state = AITLState.IDLE

    def step(self, measured):
        self.measured = measured

        # FSM
        self._update_fsm()

        # PID動作は STARTUP/RUN のときのみ
        if self.state in (AITLState.STARTUP, AITLState.RUN):
            self.control_output = self.pid.update(self.setpoint, measured)
        else:
            self.control_output = 0

        # LLM（まだ何もしない）
        if self.llm:
            self.llm.adapt(self)

        return self.control_output

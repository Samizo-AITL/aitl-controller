class FakeLLM:
    """
    A simplified model that emulates an LLM-based gain tuning mechanism
    used in the AITL architecture.

    The LLM adjusts PID gains *only when* the FSM is in the TUNE state.
    This class does not perform reasoning; it simply modifies gains
    based on the magnitude of the tracking error.

    Behavior
    --------
    - Large error  (|e| > 0.5)  → Increase gains (boost response)
    - Small error               → Slightly decay gains (stabilization phase)
    """

    # Gain adjustment ratios (constants for transparency)
    KP_UP = 1.02
    KD_UP = 1.01
    KP_DOWN = 0.995
    KD_DOWN = 0.99

    def tune(self, pid, e: float) -> None:
        """
        Adjust PID gains based on the magnitude of tracking error.

        Parameters
        ----------
        pid : PID
            PID controller instance whose gains will be modified.
        e : float
            Tracking error.

        Notes
        -----
        This method assumes it is called *only when the FSM state is TUNE*.
        """
        if e is None:
            raise ValueError("Error value e must not be None.")

        abs_e = abs(e)

        # Increase gains for large disturbance recovery
        if abs_e > 0.5:
            pid.kp *= FakeLLM.KP_UP
            pid.kd *= FakeLLM.KD_UP

        # Fine adjustment for stabilization
        else:
            pid.kp *= FakeLLM.KP_DOWN
            pid.kd *= FakeLLM.KD_DOWN

class FSM:
    """
    Finite State Machine (FSM) used in the middle layer of AITL.

    The FSM supervises the system condition based on the tracking error
    and determines whether the LLM layer should tune PID gains.

    States
    ------
    NORMAL   : Normal tracking condition.
    DISTURB  : Large disturbance detected.
    TUNE     : Recovery phase where LLM adjusts PID gains.
    """

    # State constants
    NORMAL = "NORMAL"
    DISTURB = "DISTURB"
    TUNE = "TUNE"

    def __init__(self):
        self.state = FSM.NORMAL

    # -----------------------------------
    # Reset FSM state
    # -----------------------------------
    def reset(self) -> None:
        """Reset state to NORMAL."""
        self.state = FSM.NORMAL

    # -----------------------------------
    # State transition logic
    # -----------------------------------
    def transition(self, e: float) -> str:
        """
        Transition FSM state based on the magnitude of the tracking error.

        Parameters
        ----------
        e : float
            Tracking error.

        Returns
        -------
        str
            Updated FSM state.
        """
        if e is None:
            raise ValueError("Error value e must not be None.")

        abs_e = abs(e)

        # Large error → disturbance detected
        if abs_e > 1.0:
            self.state = FSM.DISTURB

        # Disturbance recovered → enter tuning phase
        elif self.state == FSM.DISTURB and abs_e < 0.2:
            self.state = FSM.TUNE

        # Tuning completed → return to normal
        elif self.state == FSM.TUNE and abs_e < 0.05:
            self.state = FSM.NORMAL

        return self.state

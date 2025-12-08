class PID:
    """
    PID controller used as the inner loop of the AITL architecture.

    Attributes
    ----------
    kp : float
        Proportional gain.
    ki : float
        Integral gain.
    kd : float
        Derivative gain.
    i  : float
        Integral accumulator.
    prev_e : float
        Previous error value (for derivative term).
    """

    def __init__(self, kp: float, ki: float, kd: float):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.i = 0.0
        self.prev_e = 0.0

    # -----------------------------------
    # Reset internal states
    # -----------------------------------
    def reset(self) -> None:
        """Reset the integral and derivative memory."""
        self.i = 0.0
        self.prev_e = 0.0

    # -----------------------------------
    # PID computation
    # -----------------------------------
    def __call__(self, e: float, dt: float = 0.01) -> float:
        """
        Compute PID control output.

        Parameters
        ----------
        e : float
            Current error.
        dt : float
            Sampling time [s].

        Returns
        -------
        float
            PID output value.
        """
        if dt <= 0:
            raise ValueError("dt must be positive.")

        # Integral term
        self.i += e * dt

        # Derivative term
        d = (e - self.prev_e) / dt
        self.prev_e = e

        # PID output
        return self.kp * e + self.ki * self.i + self.kd * d

    # -----------------------------------
    # Helper getters (optional)
    # -----------------------------------
    @property
    def gains(self):
        """Return current PID gains as tuple (kp, ki, kd)."""
        return self.kp, self.ki, self.kd

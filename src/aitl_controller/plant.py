class Plant:
    """
    First-order lag plant model used in the AITL simulation environment.

    The continuous-time model is:

        dx/dt = (-x + u) / tau

    which represents a first-order system with time constant tau.
    Euler-forward discretization is used for numerical simulation.
    """

    def __init__(self, tau: float = 1.0):
        if tau <= 0:
            raise ValueError("Time constant tau must be positive.")
        self.x = 0.0
        self.tau = tau

    # -----------------------------------
    # Reset plant state
    # -----------------------------------
    def reset(self) -> None:
        """Reset internal state x to zero."""
        self.x = 0.0

    # -----------------------------------
    # Time update step
    # -----------------------------------
    def step(self, u: float, dt: float = 0.01) -> float:
        """
        Simulate one time step of the plant.

        Parameters
        ----------
        u : float
            Control input.
        dt : float
            Time step [s].

        Returns
        -------
        float
            Updated plant output x.
        """
        if dt <= 0:
            raise ValueError("dt must be positive.")

        dx = (-self.x + u) / self.tau
        self.x += dx * dt
        return self.x

    # -----------------------------------
    # Helper property
    # -----------------------------------
    @property
    def state(self) -> float:
        """Return current plant state x."""
        return self.x

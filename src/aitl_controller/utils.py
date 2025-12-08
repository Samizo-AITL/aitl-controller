from .fsm import FSM


def state_to_int(state: str) -> int:
    """
    Convert FSM string state to an integer for visualization or analysis.

    Mapping
    -------
    NORMAL   -> 0
    DISTURB  -> 1
    TUNE     -> 2

    Parameters
    ----------
    state : str
        FSM state as a string.

    Returns
    -------
    int
        Integer representation of the state.

    Raises
    ------
    ValueError
        If the state string is not a valid FSM state.
    """
    mapping = {
        FSM.NORMAL: 0,
        FSM.DISTURB: 1,
        FSM.TUNE: 2,
    }

    if state not in mapping:
        raise ValueError(f"Invalid FSM state: {state}")

    return mapping[state]

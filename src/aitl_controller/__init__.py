"""
AITL-Controller
----------------
A modular implementation of the AITL architecture:

    PID (Inner Loop)
    FSM (Middle Supervisory Layer)
    LLM-Based Gain Tuning (Outer Layer)

This package exposes the primary components required to build and simulate
adaptive intelligent control systems using the AITL structure.

The purpose of this file is to provide a clean and unified top-level API
so that users can simply write:

    from aitl_controller import PID, FSM, FakeLLM, Plant, AITL

instead of importing from individual modules.
"""

from .pid import PID
from .fsm import FSM
from .llm import FakeLLM
from .plant import Plant
from .controller import AITL
from .utils import state_to_int

__all__ = [
    "PID",
    "FSM",
    "FakeLLM",
    "Plant",
    "AITL",
    "state_to_int",
]

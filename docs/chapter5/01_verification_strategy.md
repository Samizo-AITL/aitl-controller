---
layout: default
title: "5.1 Verification Strategy for FSM Correctness"
---

# 5.1 Verification Strategy

FSM verification does not start with tools.
It starts with **what to check**.

---

## Three verification layers

1. **Structural checks**
   - state encoding validity
   - reset behavior
   - full assignment (no latches)

2. **Property checks**
   - invariants (state/output/transition)
   - safety constraints

3. **Behavioral checks**
   - expected sequences occur
   - Python ↔ Verilog behavior matches

Chapter5 implements all three with minimal machinery.

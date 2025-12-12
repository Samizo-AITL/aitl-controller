---
layout: default
title: "5.3 Simulation-based FSM Checking"
---

# 5.3 Simulation-based Checking

Simulation is not weak if used correctly.

---

## How simulation helps correctness

- executes assertions
- explores corner input sequences
- reveals priority and timing bugs

---

## Recommended stimulus types

1. Directed tests
   - nominal sequences
   - error/recovery paths

2. Semi-random tests
   - random commands
   - injected faults

3. Stress tests
   - rapid toggling
   - back-to-back events

---

## What simulation catches well

- missing default transitions
- output glitches
- incorrect guard priority
- reset mismatches

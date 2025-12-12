---
layout: default
title: "ASIC Checkpoints"
parent: "Chapter 3"
---

# ASIC-Flow RTL Checkpoints

## 1. Synthesizability
- No fatal errors
- No unintended latches
- No multiple drivers

## 2. Reset Determinism
- All state registers reset
- Known initial state

## 3. Transition Determinism
- Exactly one next state per cycle
- Default transition defined

## 4. Output Stability
- Moore outputs stable within cycle
- Mealy outputs intentional and checked

## 5. Clock Sanity
- Clock correctly constrained
- Reasonable clock period

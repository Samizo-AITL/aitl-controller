# ASIC-flow checkpoints — How to judge “RTL is hardware-valid”

This page is the “reading guide” for synthesis and early ASIC flow results.

## Checkpoint 1 — Synthesizability
**Pass criteria**
- RTL compiles with synthesis tool (no fatal errors)
- No unintended latch inference
- No multiple driver / tri-state misuse (unless intentionally designed)

**Typical problems**
- Incomplete assignments in combinational always blocks → latch inference
- Mixing blocking/non-blocking incorrectly → simulation vs synthesis mismatch
- Multiple always blocks driving the same reg → multiple driver

## Checkpoint 2 — Reset correctness
**Pass criteria**
- Reset defines all state-holding elements deterministically
- Reset release leads to the intended initial state
- Outputs after reset are safe (spec-defined)

**Typical problems**
- Reset deassertion not aligned with clock (if sync reset expected)
- Some registers not reset → X-propagation in simulation, unpredictable in silicon
- Async reset sensitivity list mismatch

## Checkpoint 3 — State transition determinism
**Pass criteria**
- Exactly one next-state is chosen per cycle (no ambiguous overlap unless spec-defined priority)
- Default transition (stay) is defined

**Typical problems**
- Overlapping conditions without priority definition
- Missing default branch in next-state logic

## Checkpoint 4 — Output mapping stability (Moore vs Mealy)
**Pass criteria**
- Moore outputs depend on registered state (stable within a cycle)
- Mealy outputs, if used, are intentionally combinational and validated at sampling boundary

**Typical problems**
- Combinational outputs glitching due to input hazards
- Output logic depending on “next_state” unintentionally

## Checkpoint 5 — Clock & constraints sanity (OpenLane concept)
**Pass criteria**
- Clock port correctly specified
- Clock period reasonable (not extreme)
- Reports are generated and interpretable

**Typical problems**
- “No clocks found” or unconstrained paths
- Clock name mismatch (RTL port vs constraint)
- Unrealistic clock period leading to confusing timing reports

## Checkpoint 6 — Reading typical synthesis messages
### Latch inference
If you see messages like “latch inferred”, likely you did not assign a value in all branches.

**Fix pattern**
- Provide default assignments at the top of combinational blocks
- Use `unique case` / `priority if` with explicit `default`

### Multiple drivers
Often caused by driving a signal from two always blocks.

**Fix pattern**
- Single always_ff for sequential regs
- Single always_comb for combinational

### Unused signals optimized away
Synthesis removes logic that does not affect outputs.

**Fix pattern**
- For debug-only signals, accept removal
- If you truly need a signal preserved, expose it as an output or use tool directives (advanced; out of scope)

## “RTL matches spec” — minimum proof recipe
1. From the formalized spec, select a representative set of transitions.
2. In TB, drive the inputs to trigger those transitions.
3. Check state and outputs at exact cycles.
4. Run OpenLane concept synthesis; ensure no structural warnings contradict the intended architecture.

---

Include glossary: `_includes/glossary.md`.

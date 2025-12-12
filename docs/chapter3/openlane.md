# OpenLane — Concept-level single-block ASIC flow for the FSM

## Philosophy
We use OpenLane here to confirm:
- The RTL is synthesizable
- The constraints are sane enough to produce a netlist + reports
- You can read typical warnings and understand root causes

We do **not** optimize PPA in this chapter.

## Minimal flow (concept)
Typical OpenLane steps (high-level):
1. Prep design
2. Synthesis
3. Floorplan
4. Placement
5. CTS
6. Routing
7. Reports & signoff checks (concept)

For Chapter 3, the key deliverables are:
- synthesized netlist
- timing / area reports
- warnings that teach “ASIC realism”

## Directory layout in this chapter
- `code/openlane/config.tcl`
- `code/openlane/pin_order.cfg`
- `code/openlane/README.md`

## What you must set
- Design name
- RTL source list
- Clock port name
- Clock period
- Reset strategy (async/sync) consistent with RTL

## Typical things that go wrong (and why it’s good)
- Latch inference warnings
- Multiple drivers
- Unconstrained paths
- Missing clock definition
- Reset not behaving as expected post-synthesis
- Unused logic optimizations changing debug signals

All of these are explained in `asic_checkpoints.md`.

---

Next: `asic_checkpoints.md`.

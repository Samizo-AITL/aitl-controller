# File: docs/chapter2/rtl_guidelines.md

# RTL Coding Guidelines for ASIC and OpenLane  
## FSM-Oriented Design Rules

This document defines **RTL coding guidelines** that must be followed when implementing
FSMs intended for **ASIC synthesis using OpenLane**.
The focus is on avoiding common synthesis and implementation pitfalls.

---

## General Design Goals

The RTL must be:

- Fully synthesizable
- Deterministic and complete
- Tool-friendly (Yosys / OpenLane)
- Easy to analyze and maintain

FSM code should favor **clarity and explicitness** over compactness.

---

## Clocking Rules

- Use a **single clock domain** per FSM
- Avoid gated clocks
- All state transitions must occur on the **rising edge of the clock**

### Recommended Style

```verilog
always @(posedge clk) begin
    if (reset)
        state <= S_IDLE;
    else
        state <= next_state;
end
```

---

## Reset Rules

- Use **synchronous reset**
- Reset must dominate all state transitions
- Reset behavior must be explicitly defined

### Do

- Reset FSM to a **known safe state**

### Avoid

- Asynchronous reset unless absolutely required
- Multiple reset conditions

---

## State Encoding Guidelines

- Prefer **binary encoding** for small FSMs
- Fix state encoding explicitly using `localparam`
- Do not rely on tool-generated encodings

### Rationale

- Predictable synthesis results
- Easier debugging
- Stable equivalence checking

---

## Next-State Logic Rules

- Use a **single combinational always block**
- Assign `next_state` a default value at the beginning
- Cover **all states** explicitly

### Recommended Style

```verilog
always @(*) begin
    next_state = state;
    case (state)
        S_IDLE: begin
            if (start)
                next_state = S_INIT;
        end
        default: begin
            next_state = S_IDLE;
        end
    endcase
end
```

---

## Case Statement Rules

- Always include a `default` case
- Do not use incomplete case statements
- Avoid `casex` and `casez`

### Optional (SystemVerilog)

- `unique case` may be used if formally verified

---

## Output Logic Rules

- Use **Moore-style outputs** where possible
- Derive outputs directly from the state
- Prefer continuous assignments (`assign`)

### Example

```verilog
assign mode_run = (state == S_RUN);
```

---

## Forbidden Constructs

The following constructs must **not** be used:

- Blocking delays (`#`)
- Event controls inside combinational logic
- Dynamic loops
- Non-constant `for` loops
- Latches (intentional or accidental)
- Mixed blocking / non-blocking assignments in the same always block

---

## Signal Naming Guidelines

- Use descriptive, lower_snake_case signal names
- Prefix state symbols with `S_`
- Avoid single-letter signals except for clocks

---

## Verification Readiness

Even though verification is out of scope for this chapter,
the RTL should be written so that:

- Simulation is straightforward
- Testbench signals map clearly to FSM inputs
- State observation is easy

---

## Summary

Following these guidelines ensures that:

- FSM RTL is robust and synthesizable
- OpenLane tools behave predictably
- Future integration and verification are simplified

These rules apply to **all FSM RTL code** in the AITL Silicon Pathway.

---

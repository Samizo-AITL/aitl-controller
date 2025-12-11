---
title: "Getting Started — Chapter 1 Python Baseline"
layout: default
nav_order: 6
description: "How to install, run, and simulate the AITL Chapter 1 Python baseline model."
---

# 🚀 Getting Started — AITL Chapter 1 Python Baseline

This guide explains **how to set up and run** the Python baseline model for AITL Chapter 1.  
You will install dependencies, execute the main controller, and run simulations for step response and fault scenarios.

---

# 1️⃣ Prerequisites

- Python 3.9+ (3.10/3.11 also recommended)  
- pip available in your PATH  
- Git (optional but recommended)  

---

# 2️⃣ Project Layout (Recap)

Make sure your repository contains:

```
aitl-silicon-pathway/
├── chapter1_python_model/
│   ├── src/
│   ├── sim/
│   ├── plots/
│   ├── tests/
│   ├── main.py
│   └── requirements.txt
└── docs/
    └── chapter1/
        ├── index.md
        ├── overview.md
        ├── python_model.md
        ├── fsm.md
        ├── api.md
        └── getting_started.md
```

All commands below assume you start from:

```bash
cd aitl-silicon-pathway/chapter1_python_model
```

---

# 3️⃣ Installing Dependencies

From inside `chapter1_python_model`:

```bash
# (Optional but recommended) create virtual environment
python -m venv venv

# Activate venv (Windows)
venv\Scripts\activate

# Activate venv (Linux / macOS)
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

Typical contents of `requirements.txt`:

```text
numpy
matplotlib
```

You can extend this list if you add more tooling later.

---

# 4️⃣ Running the Main Demo

The simplest way to verify the controller is working:

```bash
python main.py
```

This script typically:

- Instantiates the PID controller  
- Instantiates the AITLController (PID + FSM)  
- Runs a short simulation loop  
- Prints or plots basic behavior  

If everything is configured correctly, you should see:

- No Python errors  
- A simple demonstration of state transitions and PID output  

---

# 5️⃣ Running the Step Response Simulation

This scenario evaluates **dynamic response** of the closed-loop system to a step setpoint.

From `chapter1_python_model`:

```bash
python sim/run_step_response.py
```

Expected behavior:

- The script runs a time-step loop  
- The controller transitions from IDLE → STARTUP → RUN  
- PID responds to a step change in setpoint  
- A plot window opens showing:
  - Process variable (x(t))
  - Control signal (u(t))
- A PNG file is saved in `plots/`, e.g.:

```
plots/step_response_YYYYMMDD_HHMMSS.png
```

If a window does not appear, check:

- matplotlib backend configuration  
- Whether you are in a headless environment (e.g., remote server)

---

# 6️⃣ Running the Fault Scenario Simulation

This scenario verifies **fault handling and supervisory logic**.

From `chapter1_python_model`:

```bash
python sim/run_fault_scenario.py
```

Expected behavior:

- The controller starts from IDLE  
- Moves through STARTUP to RUN  
- At a predefined time, `error_detected` is triggered  
- FSM transitions to FAULT  
- PID output is forced to zero  
- Optionally, a later `reset_cmd` returns FSM to IDLE  

A plot is generated, typically including:

- Process variable x(t)  
- FSM state (plotted as numeric code)  

And a PNG is saved under:

```
plots/fault_scenario_YYYYMMDD_HHMMSS.png
```

---

# 7️⃣ Saving Plots and Using Them in Docs

All simulation scripts are designed to:

- **Show** the plot using `plt.show()`  
- **Save** the plot as a PNG into the `plots/` directory  

You can then move or copy selected plots into:

```
docs/chapter1/images/
```

for use in documentation pages (e.g. `python_model.md`, `fsm.md`).

---

# 8️⃣ Running Tests (Optional but Recommended)

If you have unit tests under `tests/`, you can run:

```bash
python -m pytest
```

or

```bash
pytest
```

Common tests include:

- PID numerical behavior  
- FSM transition correctness  
- Controller integration behavior  

This is especially useful **before**:

- Modifying PID gains  
- Changing FSM rules  
- Starting RTL conversion in Chapter 2  

---

# 9️⃣ Troubleshooting

### ❓ `ModuleNotFoundError: No module named 'src'`

Make sure you are running commands from `chapter1_python_model`:

```bash
cd aitl-silicon-pathway/chapter1_python_model
python sim/run_step_response.py
```

and that the project is structured exactly as shown in the directory listing above.

---

### ❓ No plots saved / blank plots

- Verify `plots/` directory exists or is created by the script (`os.makedirs("plots", exist_ok=True)`)  
- Check that the simulation loop actually runs for enough steps  
- Confirm matplotlib is installed and functional  

---

# 🔗 How This Connects to Later Chapters

The code and behavior you run here will later be:

- Translated into **Verilog RTL** (Chapter 2)  
- Passed through **synthesis and place-and-route** (Chapter 3)  
- Extracted into **SPICE netlists** (Chapter 4)  
- Verified via **waveform and timing analysis** (Chapter 5)  

The Python model is the **golden reference**.  
If you change it, you must also update RTL and verification flows.

---

# ✅ Summary

In this Getting Started guide, you:

- Set up a Python environment  
- Installed dependencies  
- Ran the main AITL controller demo  
- Executed step response and fault simulations  
- Generated plots for use in Chapter 1 documentation  
- Prepared the environment for the next step: **FSM → RTL (Chapter 2)**

You are now ready to move deeper into the AITL Silicon Pathway.

---

# © AITL Silicon Pathway Project


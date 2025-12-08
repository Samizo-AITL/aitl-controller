# AITL-Controller
**Adaptive Intelligent Three-Layer Control Architecture (AITL)**  
A lightweight Python implementation of a structured control architecture integrating:

- **PID** — Inner-loop real-time stabilization  
- **FSM** — Middle-layer supervisory mode switching  
- **LLM** — Outer-layer adaptive PID tuning  

This project provides a clean minimal working example (MWE) for combining classical control systems with AI reasoning components while maintaining safety, interpretability, and modularity.

---

## Features

- ✔ Three-layer control: PID × FSM × LLM  
- ✔ Well-structured Python package (`src/aitl_controller/`)  
- ✔ Demo programs for simulation  
- ✔ Full pytest test suite  
- ✔ MIT License (free for academic & commercial use)

---

## Installation

```bash
git clone https://github.com/<YOUR-REPO>/aitl-controller
cd aitl-controller
pip install -e .
```

---

## Quick Example

```python
from aitl_controller import PID, FSM, FakeLLM, Plant, AITL

plant = Plant()
pid = PID(1.0, 0.2, 0.01)
fsm = FSM()
llm = FakeLLM()
ctl = AITL(pid, fsm, llm)

for t in range(1000):
    r = 1.0
    x = plant.x
    u, state = ctl.step(r, x, dt=0.01)
    plant.step(u, dt=0.01)
    print(t, x, state)
```

---

## Directory Structure

```plaintext
aitl-controller/
│
├── src/aitl_controller/
│   ├── pid.py
│   ├── fsm.py
│   ├── llm.py
│   ├── plant.py
│   ├── controller.py
│   ├── utils.py
│   └── __init__.py
│
├── demos/
│   ├── simple_demo.py
│   ├── disturbance_demo.py
│   ├── tracking_demo.py
│   └── tuning_demo.py
│
├── tests/
│   ├── test_pid.py
│   ├── test_fsm.py
│   ├── test_llm.py
│   ├── test_plant.py
│   └── test_controller.py
│
├── assets/css/style.css
├── LICENSE
└── pyproject.toml
```

---

## License

MIT License  
© 2025 Shinichi Samizo

---

## Documentation

https://samizo-aitl.github.io/EduController/

---
title: "Chapter 1 Overview"
layout: default
nav_order: 1
parent: "AITL Documentation"
description: "Full conceptual overview of the AITL Python baseline model"
---

# Chapter 1 — Overview  
*Complete conceptual foundation of the AITL Python Baseline Model*

-------------------------------------------------------------

## Purpose of Chapter 1
This chapter establishes the baseline mathematical and architectural model of the AITL system:
a three-layer control architecture designed for hybrid intelligence systems that must operate
both in real-time (PID/FSM) and high-level autonomy (LLM).

This Python model serves as:
- reference implementation for hardware chapters  
- behavioral “golden model”  
- formal specification for FSM → RTL  
- educational bridge between software and silicon  

-------------------------------------------------------------

## What Is AITL?
AITL = Adaptive Intelligent Three-Layer architecture

Layers:
1. PID – Real-time low-level numeric control  
2. FSM – Supervisory mode/state management  
3. LLM – High-level reasoning, adaptation, redesign  

Only PID + FSM are implemented in Chapter 1.

-------------------------------------------------------------

## Layer Architecture

### PID Layer
Classical control law:

    u = Kp * e + Ki * integral(e) + Kd * derivative(e)

Discrete-time version implemented in Python.

### FSM Layer
Supervisory control with states:

    IDLE → STARTUP → RUN → FAULT → IDLE

Transitions depend on:
- user commands  
- completion flags  
- error detection  

### LLM Layer (placeholder)
Future responsibilities:
- tuning PID  
- rewriting FSM  
- evaluating system health  
- predictive optimization  

-------------------------------------------------------------

## Relationship to the AITL Silicon Pathway

This chapter is the first step of the end-to-end hardware education pipeline:

Python → Verilog (RTL) → OpenLane → GDSII → Magic RC Extraction → SPICE

The behaviors defined here *must be preserved* in all downstream flows.

-------------------------------------------------------------

## Deliverables of Chapter 1
- Full Python model (`src/`)
- Simulation harness (`sim/`)
- Plots (step response, fault scenario)
- Formal FSM specification
- API contract for RTL design

-------------------------------------------------------------

## Role in Chapter 2 (FSM → RTL)
This chapter provides formal definitions for:
- states  
- transitions  
- conditions  
- input/output signal semantics  
- correct behavior of RUN / STARTUP / FAULT  

These definitions must be faithfully translated to the RTL.

-------------------------------------------------------------

## Recommended Reading Order
1. overview.md  
2. python_model.md  
3. fsm.md  
4. api.md  
5. getting_started.md  

-------------------------------------------------------------

## Summary
Chapter 1 defines the golden behavioral model.  
All future hardware chapters must match this behavior exactly.

-------------------------------------------------------------

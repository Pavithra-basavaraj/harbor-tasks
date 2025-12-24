# Harbor Task – New Hire Assignment

## Overview
This repository contains my solution for the **Harbor New Hire Assignment**.  
The task implements a **simple data-processing Harbor task** that reads an input file, processes the data, and writes the result to an output file, strictly following Harbor framework guidelines.

The task is designed to:
- Pass the **Oracle validation test (1.0)**
- Fail the **NOP validation test (0.0)**
- Comply with **Docker, linting, and task-structure requirements**

---

## Task Description
- **Type:** Data Processing Task  
- **Difficulty:** Easy / Medium  
- **Functionality:**  
  - Reads input data from an absolute path (`/app/input.txt`)
  - Processes the data using a script
  - Writes the processed result to `/app/output.txt`

---

## Folder Structure
harbor_tasks/<task-name>/
├── task.toml # Task metadata and resource configuration
├── instruction.md # Instructions provided to the agent
├── environment/
│ ├── Dockerfile # Container environment
│ └── input.txt # Input data file
├── solution/
│ └── solve.sh # Reference solution
└── tests/
├── test.sh # Test runner
└── test_outputs.py # Validation tests

## Prerequisites
Ensure the following tools are installed:
- **Docker**
- **uv**
- **WSL (for Windows users)**

--Verify installation:
 docker --version
 uv --version
 
--How to Run Validation Testss
uv sync

--Oracle Test (Expected: 1.0)
uv run harbor run --agent oracle --path harbor_tasks/<task-name> --job-name test-oracle

--NOP Test (Expected: 0.0)
uv run harbor run --agent nop --path harbor_tasks/<task-name> --job-name test-nop

--Linting
uvx ruff check harbor_tasks/<task-name>

--Compliance Checklist
Uses absolute paths (/app/...)
Output is computed in solve.sh (no hardcoded values)
task.toml includes required fields:
memory_mb
storage_mb
Dockerfile does not copy tests/ or solution/
Dockerfile does not install pytest
Oracle test returns 1.0
NOP test returns 0.0
Ruff linting passes

--Notes
All instructions and tests strictly follow Harbor documentation.
The task is intentionally designed to avoid auto-passing under the NOP agent.
Required canary GUIDs are included where applicable.

--Submission
A pull request is created under:new-hire/<your-name>/task
Oracle and NOP test outputs are included in the pull request description.
Assignment is submitted within 24 hours as instructed.

Author: Pavithra S B
Purpose: Hiring Assignment – Harbor Task Creation

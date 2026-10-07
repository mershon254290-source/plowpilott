# ⚡ FlowPilot

**AI Business Process Automation Consultant**

FlowPilot is a lightweight AI-assisted tool that analyzes manual business processes, identifies automation opportunities, recommends AI agents, and estimates automation potential.

It is built as a practical portfolio project around **Python, Streamlit, Ollama, process analysis, automation logic, and workflow design**.

## 🎯 Why I Built FlowPilot

Many business processes contain repetitive work such as:

- checking documents
- entering and updating records
- sending emails
- requesting approvals
- creating accounts
- following up on missing information
- moving information between systems

FlowPilot explores how these processes can be divided between:

**Human work → AI-assisted work → deterministic automation**

The goal is not to automate every decision. High-risk decisions, approvals, exceptions, and sensitive actions should remain subject to human review.

## 🚀 What FlowPilot Does

A user describes a manual business process.

FlowPilot then:

1. Analyzes the process with an LLM.
2. Summarizes the process.
3. Identifies repetitive tasks.
4. Identifies bottlenecks and risks.
5. Suggests automation opportunities.
6. Recommends relevant AI agents.
7. Generates a proposed automation workflow.
8. Calculates a deterministic automation-potential score.
9. Explains the signals behind the score.
10. Provides a high-level automation recommendation.

## 🧩 Example: HR Employee Onboarding

### Input

> HR receives a new employee's information, checks the documents, creates an employee record, requests IT account creation, sends onboarding instructions, and follows up on missing documents.

### FlowPilot identifies opportunities such as

- document verification
- employee record creation
- IT account requests
- onboarding communication
- missing-document follow-up

It can then propose a workflow containing automation and human-review points.

## 🏗️ Current Architecture

```text
User
  ↓
Streamlit UI
  ↓
Process Description
  ↓
Ollama / Local LLM
  ↓
AI Process Analysis
  ↓
Deterministic Scoring Engine
  ↓
Automation Potential
  ↓
Human-in-the-Loop Recommendation
```

### Current stack

- **Python**
- **Streamlit**
- **Ollama**
- **Qwen 2.5 0.5B**
- **Git / GitHub**

## 📊 Scoring Approach

The automation score is calculated separately from the LLM output so that the same process produces a consistent score.

The scoring engine considers signals related to:

- Manual Work
- Repetition
- Rule-Based Decisions
- Error Reduction
- System Integration
- AI Suitability

The score is intended as an assessment signal rather than a financial or operational guarantee.

## 👤 Human-in-the-Loop

FlowPilot does not assume that every business task should be fully automated.

A realistic automation system may combine:

```text
AI Agent
    ↓
Validation
    ↓
Human Approval
    ↓
Automation
    ↓
Notification
```

This is especially important for sensitive HR, financial, compliance, and operational decisions.

## 🛠️ Running Locally

### Requirements

- Python 3.x
- Ollama
- A local Ollama model
- Streamlit

### Install dependencies

```bash
pip install streamlit ollama
```

### Pull the model

```bash
ollama pull qwen2.5:0.5b
```

### Run FlowPilot

```bash
streamlit run flowpilot_app.py
```

## 📁 Project Structure

```text
FlowPilot/
├── flowpilot_app.py
├── README.md
├── .gitignore
└── docs/
    ├── 01_Product_Overview.md
    ├── 02_Product_Requirements.md
    ├── 03_System_Architecture.md
    └── 04_User_Flow.md
```

## 🔭 Future Direction

The current version intentionally focuses on the core analysis experience.

Potential future improvements include:

- task-level Human / AI / Automation classification
- ranked automation opportunities
- impact vs. effort analysis
- interactive workflow visualization
- ROI estimation
- API and webhook integrations
- connectors to business systems
- executable workflows
- stronger evaluation and testing
- modular backend architecture

These are future directions, not claims about functionality already implemented.

## 💡 Portfolio Context

FlowPilot is a practical project demonstrating an interest in:

- AI automation
- business process analysis
- workflow design
- AI agents
- human-in-the-loop systems
- Python development
- product thinking

The project is intentionally being developed incrementally: first understanding the business problem, then improving the analysis, and eventually connecting recommendations to real automation systems.

## 📌 Project Status

**Current stage:** Working MVP / Portfolio Project

The priority at this stage is learning, demonstrating practical ability, and validating the approach through real-world problems.

## 👨‍💻 Author

Built by **Ali** as an independent AI automation project.

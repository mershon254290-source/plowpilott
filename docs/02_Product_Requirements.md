# FlowPilot — Product Requirements

## 1. Purpose

This document defines the functional and non-functional requirements for FlowPilot.

The purpose is to establish a clear product scope for the MVP and provide a foundation for future development.

---

# 2. Product Goal

FlowPilot should allow a business user to describe a manual business process and receive an actionable automation assessment.

The system should answer:

* What tasks exist in the process?
* Which tasks are repetitive?
* Which tasks are suitable for automation?
* Which tasks could use AI?
* Where should humans remain involved?
* How suitable is the process for automation?
* What could an automated workflow look like?

---

# 3. MVP Scope

The MVP focuses on process analysis and automation assessment.

The MVP includes:

* Process input
* AI analysis
* Task extraction
* Task classification
* Automation scoring
* Automation opportunities
* AI agent recommendations
* Human-in-the-loop recommendations
* Workflow recommendations

The MVP does not execute business workflows.

---

# 4. User

The primary MVP user is a business professional who understands a manual business process but may not have technical automation expertise.

Examples:

* Business owner
* Operations manager
* HR manager
* Finance manager
* Automation consultant
* Process improvement specialist

---

# 5. User Input

The user should be able to enter a natural-language description of a business process.

Example:

> HR receives employee documents by email, enters the employee information into the HR system, sends onboarding forms, and notifies IT to create accounts.

The input should not require technical knowledge.

---

# 6. Functional Requirements

## FR-01 — Process Input

The system must provide a text input area where the user can describe a business process.

### Acceptance Criteria

* User can enter multi-line text.
* User can describe the process in natural language.
* The system should accept processes of different business types.

---

## FR-02 — Process Analysis

The system must analyze the submitted process using an AI model.

### Acceptance Criteria

The analysis should produce:

* Process summary
* Tasks
* Bottlenecks
* Automation opportunities
* AI agent recommendations
* Workflow recommendation

---

## FR-03 — Task Extraction

The system must identify individual tasks within the process.

### Acceptance Criteria

Each identified task should be represented separately.

Example:

```text
Task 1: Receive employee documents
Task 2: Enter employee data
Task 3: Send onboarding forms
Task 4: Notify IT
```

---

## FR-04 — Task Classification

The system should classify identified tasks.

Initial categories include:

* Data Entry
* Communication
* Validation
* Input
* Decision
* System Update
* Other

---

## FR-05 — Automation Potential

Each task should receive an automation potential classification.

Initial levels:

* High
* Medium
* Low

---

## FR-06 — Automation Score

FlowPilot must calculate an overall automation score.

The score should provide a simple way to prioritize processes.

The MVP should favor deterministic scoring logic where possible rather than relying entirely on an AI-generated number.

### Example

```text
Automation Score: 78/100
```

---

## FR-07 — Automation Opportunities

The system should identify practical opportunities to automate the process.

Examples:

* Automatically extract information from documents
* Automatically update business systems
* Automatically send notifications
* Automatically validate information
* Automatically route tasks

---

## FR-08 — AI Agent Recommendations

FlowPilot should recommend AI agents when appropriate.

Each recommendation should describe:

* Agent name
* Agent role
* Tasks performed
* Expected value

Example:

```text
Agent: Document Processing Agent

Role:
Extract employee information from submitted documents.

Tasks:
- Read documents
- Extract structured information
- Validate required fields
- Send structured data to the HR system
```

---

## FR-09 — Human-in-the-Loop

The system should identify tasks where human involvement is recommended.

Examples:

* Final approval
* Exceptional cases
* Sensitive decisions
* Ambiguous information
* Policy-based decisions

---

## FR-10 — Workflow Recommendation

The system should produce a high-level workflow.

Example:

```text
Employee Documents
        ↓
Document Processing Agent
        ↓
Validation
        ↓
Human Review
        ↓
HR System Update
        ↓
IT Notification
```

---

## FR-11 — Recommendation

FlowPilot should provide a final recommendation describing whether the process appears suitable for automation.

Example outcomes:

* High automation potential
* Moderate automation potential
* Low automation potential

The recommendation should be based on the analysis and scoring system.

---

# 7. User Experience Requirements

## UX-01 — Simplicity

The interface should be simple enough for a non-technical business user.

The user should not need knowledge of:

* APIs
* Programming
* AI models
* Workflow engines

---

## UX-02 — Clear Results

Analysis results should be organized into clear sections.

Recommended sections:

1. Process Summary
2. Automation Score
3. Task Analysis
4. Automation Opportunities
5. AI Agents
6. Human-in-the-Loop
7. Workflow
8. Final Recommendation

---

## UX-03 — Explainability

The system should explain why a process receives a particular automation assessment.

Users should be able to understand the main factors behind the recommendation.

---

# 8. Non-Functional Requirements

## NFR-01 — Performance

The application should provide results within a reasonable time for normal business-process descriptions.

---

## NFR-02 — Reliability

The application should handle incomplete or poorly structured process descriptions without crashing.

---

## NFR-03 — Security

The application must avoid exposing sensitive business information.

The system should not store sensitive user input unless explicitly designed to do so.

API keys, passwords, tokens, and secrets must never be committed to GitHub.

---

## NFR-04 — Maintainability

The codebase should be structured so that the following components can evolve independently:

* AI analysis
* Task extraction
* Scoring
* Workflow generation
* User interface

---

## NFR-05 — Extensibility

The architecture should allow future integrations with:

* CRM systems
* HR systems
* ERP systems
* Email
* Databases
* Workflow automation platforms
* Business APIs

---

# 9. MVP Limitations

The MVP will intentionally not attempt to solve every automation problem.

The MVP will not initially:

* Execute workflows
* Modify external business systems
* Automatically send emails
* Create accounts
* Deploy AI agents
* Integrate with every business application
* Guarantee that an automation recommendation is correct

The MVP is an **analysis and recommendation system**, not yet an execution platform.

---

# 10. Future Requirements

Future versions may include:

### Workflow Visualization

Interactive visual representation of the proposed workflow.

### Automation Blueprint

Generate a detailed technical automation plan.

### Workflow Execution

Allow users to deploy selected workflows.

### Integrations

Connect with business systems such as:

* Gmail
* Microsoft 365
* Slack
* Salesforce
* HubSpot
* SAP
* HR platforms
* Accounting platforms

### Analytics

Measure:

* Time saved
* Tasks automated
* Error reduction
* Cost reduction
* Workflow performance

### Industry Templates

Provide specialized process analysis for:

* HR
* Finance
* Customer Service
* Sales
* Real Estate
* Logistics
* E-commerce

---

# 11. Product Success Metrics

Potential product metrics include:

### Process Analysis Completion Rate

Percentage of submitted processes that receive a successful analysis.

### Recommendation Usefulness

Percentage of users who consider the automation recommendations useful.

### Automation Opportunity Identification

Number of actionable automation opportunities identified.

### Assessment-to-Implementation Rate

Percentage of analyzed processes that eventually become automation projects.

### Time Saved

Estimated operational time saved through recommended or implemented automation.

---

# 12. Product Principle

The core principle of FlowPilot is:

> **Understand the process first. Automate second.**

FlowPilot should not recommend automation simply because a task can technically be automated.

The system should consider:

* Business value
* Repetition
* Rules
* Error potential
* Integration requirements
* AI suitability
* Human judgment

The objective is to recommend automation that is practical, valuable, and controllable.

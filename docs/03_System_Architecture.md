FlowPilot — System Architecture
1. Overview

FlowPilot is an AI-assisted business process analysis application.

The system receives a natural-language description of a business process, analyzes it using an AI model, extracts and classifies tasks, calculates an automation score, and generates recommendations for AI agents and workflow automation.

The current architecture is intentionally lightweight to support rapid MVP development.

2. High-Level Architecture

The current system consists of the following major components:

┌─────────────────────────────┐
│        User Interface       │
│          Streamlit          │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      Process Input Layer    │
│   Natural Language Input    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       AI Analysis Layer     │
│         Ollama / Qwen       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      Task Extraction        │
│      & Classification        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       Scoring Engine        │
│ Deterministic Assessment    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Recommendation Engine       │
│ Agents / Human / Workflow   │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       Results UI             │
│ Score / Tasks / Workflow    │
└─────────────────────────────┘
3. Component Architecture
3.1 User Interface
Technology

Streamlit

Responsibilities

The UI is responsible for:

Displaying the FlowPilot interface
Accepting process descriptions
Triggering analysis
Displaying analysis results
Displaying automation scores
Displaying recommendations
Displaying workflow information

The UI should remain simple and business-user friendly.

4. Process Input Layer

The input layer accepts a business process described using natural language.

Example:

HR receives employee documents by email,
enters the information into the HR system,
sends onboarding forms,
and notifies IT.

The input is passed to the AI analysis layer.

5. AI Analysis Layer
Technology

The current MVP uses:

Ollama
Qwen 2.5
Local model execution

The AI layer is responsible for qualitative process analysis.

It identifies:

Process summary
Tasks
Bottlenecks
Automation opportunities
AI agent opportunities
Workflow suggestions
6. Why AI Is Not Responsible for the Final Score

The AI model is used primarily for understanding the process.

The final automation score should not depend entirely on an AI-generated number.

Small local models may produce inconsistent numerical outputs.

Therefore, FlowPilot separates:

AI Reasoning
     +
Deterministic Scoring

The AI identifies and describes tasks.

The scoring engine evaluates the tasks using explicit rules.

This improves consistency and explainability.

7. Task Extraction Layer

The task extraction layer identifies individual tasks from the AI response.

Example:

TASK 1: Receive employee documents
TASK 2: Enter employee information
TASK 3: Send onboarding forms
TASK 4: Notify IT

The system extracts these tasks and removes duplicate entries.

8. Task Classification Layer

Each task is classified according to its operational nature.

Current categories include:

Category	Description
Data Entry	Entering or transferring information
Communication	Sending messages or notifications
Validation	Checking or verifying information
Input	Receiving information
Decision	Making a business decision
System Update	Updating a business system
Other	Tasks that do not match existing categories

The classification layer also estimates automation potential.

9. Automation Potential

Each task receives an initial automation potential.

High
Medium
Low

The classification is based on task characteristics and keywords.

Example:

Enter employee data
→ Data Entry
→ High automation potential

While:

Approve employee exception
→ Decision
→ Lower automation potential
10. Scoring Engine

The scoring engine calculates an overall automation score.

The score is based primarily on task automation potential.

Example weighting:

High    = 1.0
Medium  = 0.6
Low     = 0.2

The task score is converted into a 0–100 scale.

Integration-related signals may provide an additional bonus.

The final score is capped at 100.

11. Recommendation Engine

The recommendation layer converts analysis results into practical recommendations.

It considers:

Task types
Automation potential
System integrations
AI suitability
Human decision points

The output may include:

Recommended AI agents
Automation opportunities
Human-in-the-loop points
Suggested workflow
12. AI Agent Layer

FlowPilot can recommend specialized AI agents.

Examples:

Document Processing Agent

Handles:

Document reading
Information extraction
Data structuring
Data Entry Agent

Handles:

Data transfer
Form population
System updates
Communication Agent

Handles:

Email generation
Notifications
Status updates
Validation Agent

Handles:

Data validation
Required-field checks
Rule-based verification

The current MVP recommends agents but does not execute them.

13. Human-in-the-Loop Layer

Not every task should be automated.

FlowPilot should identify points where human review remains useful.

Examples:

AI Agent
   ↓
Validation
   ↓
Human Approval
   ↓
System Update

Human involvement may be required for:

Approvals
Exceptions
Sensitive decisions
Ambiguous cases
Business judgment
14. Workflow Layer

The workflow layer represents how tasks could be connected in an automated process.

Example:

Employee Documents
        ↓
Document Processing Agent
        ↓
Data Validation
        ↓
Human Review
        ↓
HR System Update
        ↓
IT Notification

The current MVP generates a conceptual workflow.

Future versions will transform this into an interactive workflow visualization.

15. Current Data Flow

The current data flow is:

User Input
    ↓
AI Prompt
    ↓
Ollama
    ↓
AI Response
    ↓
Task Extraction
    ↓
Task Classification
    ↓
Automation Scoring
    ↓
Recommendations
    ↓
Streamlit Results
16. Technology Stack
Frontend

Streamlit

Backend

Python

AI Runtime

Ollama

AI Model

Qwen 2.5

Version Control

Git

Repository

GitHub

17. Current Architecture Limitations

The current MVP has several limitations.

Single Application File

Most application logic currently exists in:

flowpilot_app.py

This is acceptable for the MVP but should eventually be separated into modules.

Basic Task Classification

Current classification relies partly on keyword-based logic.

Future versions should use a stronger classification system.

Basic Scoring

The current scoring engine is rule-based and intentionally simple.

Future versions should incorporate more business-oriented factors.

No Persistent Database

The MVP does not currently maintain a database of analyzed processes.

No Workflow Execution

The system generates recommendations but does not execute workflows.

Limited Integrations

The MVP does not yet connect directly to external business systems.

18. Future Architecture

As FlowPilot grows, the architecture should evolve toward modular services.

A possible future architecture:

                    ┌──────────────────┐
                    │   Web Interface  │
                    │     Streamlit    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   API / Backend  │
                    └────────┬─────────┘
                             │
          ┌──────────────────┼──────────────────┐
          ▼                  ▼                  ▼
 ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
 │ Process Engine │ │ Scoring Engine │ │ Agent Engine   │
 └────────────────┘ └────────────────┘ └────────────────┘
          │                  │                  │
          └──────────────────┼──────────────────┘
                             ▼
                    ┌──────────────────┐
                    │ Workflow Engine  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Integrations     │
                    │ CRM / HR / ERP   │
                    │ Email / APIs     │
                    └──────────────────┘
19. Architecture Principles

FlowPilot should follow these principles:

Separation of Concerns

AI analysis, scoring, workflow generation, and UI should eventually be separate components.

Deterministic Core Logic

Important business calculations should use predictable rules where possible.

AI-Assisted Reasoning

AI should be used where natural-language understanding and reasoning provide value.

Explainability

Recommendations should be understandable to business users.

Human Control

Critical business decisions should support human review.

Extensibility

The architecture should allow additional models, integrations, and workflow engines in the future.

20. Architectural Direction

The architecture should evolve gradually.

The immediate objective is not to build a complex distributed platform.

The priority is:

Reliable MVP
     ↓
Modular Application
     ↓
Workflow Visualization
     ↓
Automation Blueprint
     ↓
Workflow Execution
     ↓
Automation Platform

The architecture should therefore remain simple while preserving clear boundaries between major product capabilities.
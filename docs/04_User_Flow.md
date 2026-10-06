# FlowPilot — User Flow

## 1. Overview

This document describes the expected user journey through FlowPilot.

The primary objective is to make the process analysis experience simple for a non-technical business user.

The user should be able to describe a business process, request an analysis, and understand the resulting automation opportunities without requiring technical knowledge.

---

# 2. Primary User Journey

The primary FlowPilot journey is:

```text
Open FlowPilot
      ↓
Describe Business Process
      ↓
Start Analysis
      ↓
AI Process Analysis
      ↓
Task Extraction
      ↓
Task Classification
      ↓
Automation Scoring
      ↓
AI Agent Recommendations
      ↓
Human-in-the-Loop Analysis
      ↓
Workflow Recommendation
      ↓
Final Automation Recommendation
```

---

# 3. Step 1 — Open FlowPilot

The user opens the FlowPilot application.

The interface should immediately communicate:

* What FlowPilot does
* What the user needs to provide
* What type of result they will receive

The interface should remain simple and focused.

---

# 4. Step 2 — Describe the Business Process

The user enters a description of an existing manual process.

Example:

```text
HR receives new employee documents by email.
The HR team enters the employee information into the HR system.
They send onboarding forms to the employee.
Finally, HR notifies IT so that accounts can be created.
```

The user does not need to structure the process manually.

Natural language is the primary input format.

---

# 5. Step 3 — Start Analysis

The user selects:

```text
Analyze Process
```

FlowPilot sends the process description to the AI analysis layer.

The application should provide feedback that analysis is in progress.

---

# 6. Step 4 — AI Process Analysis

The AI analyzes the submitted process.

The AI attempts to identify:

* Process purpose
* Individual tasks
* Bottlenecks
* Repetitive work
* Automation opportunities
* Potential AI agents
* Workflow structure

The AI output is treated as an analytical input rather than the final source of truth for numerical scoring.

---

# 7. Step 5 — Task Extraction

FlowPilot extracts individual tasks from the AI analysis.

Example:

```text
Task 1
Receive employee documents

Task 2
Enter employee information

Task 3
Send onboarding forms

Task 4
Notify IT
```

Duplicate tasks should be removed.

---

# 8. Step 6 — Task Classification

Each task is classified.

Example:

| Task                  | Category      | Automation Potential |
| --------------------- | ------------- | -------------------- |
| Receive documents     | Input         | Medium               |
| Enter employee data   | Data Entry    | High                 |
| Send onboarding forms | Communication | High                 |
| Notify IT             | Communication | High                 |

The classification helps the scoring engine evaluate the process.

---

# 9. Step 7 — Automation Score

The scoring engine calculates an automation score.

Example:

```text
Automation Score
78 / 100
```

The score should help the user understand the overall automation potential of the process.

The score should be explainable.

The user should be able to understand the main factors contributing to the result.

---

# 10. Step 8 — Automation Opportunities

FlowPilot presents practical opportunities for automation.

Example:

```text
• Automatically extract employee information from documents.
• Automatically populate the HR system.
• Automatically send onboarding forms.
• Automatically notify IT.
```

The goal is to move from abstract AI suggestions to practical business actions.

---

# 11. Step 9 — AI Agent Recommendations

FlowPilot identifies potential AI agents.

Example:

```text
Document Processing Agent
    ↓
Extract employee information

Data Entry Agent
    ↓
Update HR system

Communication Agent
    ↓
Send onboarding notifications
```

Each agent recommendation should explain its role.

---

# 12. Step 10 — Human-in-the-Loop

FlowPilot identifies where human involvement should remain.

Example:

```text
Document Processing Agent
          ↓
      Validation
          ↓
    Human Review
          ↓
      HR System
```

Human review may be recommended for:

* Exceptions
* Sensitive information
* Approvals
* Ambiguous cases
* Business decisions

---

# 13. Step 11 — Workflow Recommendation

FlowPilot presents a conceptual automated workflow.

Example:

```text
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
```

The current MVP presents the workflow conceptually.

Future versions will provide an interactive visual workflow.

---

# 14. Step 12 — Final Recommendation

FlowPilot provides a final assessment.

Possible outcomes include:

### High Automation Potential

The process contains many repetitive, predictable, and system-based tasks.

### Moderate Automation Potential

Some parts of the process are suitable for automation while others require human involvement.

### Low Automation Potential

The process contains significant human judgment, complex decisions, or highly variable activities.

The recommendation should be based on the task analysis and scoring engine.

---

# 15. Error and Edge Cases

FlowPilot should handle common problems gracefully.

## Empty Input

If the user submits no process description, the system should ask them to provide a process.

## Very Short Input

If the process description is too short to analyze meaningfully, the system should request additional information.

## Poorly Structured Input

The system should attempt to interpret natural-language descriptions even when the process is not written as a numbered list.

## AI Failure

If the AI model fails to respond, the application should display a clear error instead of crashing.

## Incomplete AI Output

If the AI does not provide all expected sections, the application should still display whatever information can be safely extracted.

---

# 16. User Experience Principles

## Simple

The user should not need technical knowledge.

## Transparent

The system should explain its recommendations.

## Actionable

Results should help the user decide what to automate.

## Controlled

The system should clearly distinguish recommendations from actual automation execution.

## Business-Oriented

The interface should focus on business outcomes rather than AI terminology.

---

# 17. Future User Flow

The future product may extend the journey to:

```text
Process Discovery
       ↓
Automation Assessment
       ↓
Automation Blueprint
       ↓
Workflow Visualization
       ↓
User Approval
       ↓
Workflow Deployment
       ↓
Workflow Execution
       ↓
Monitoring
       ↓
Optimization
```

This represents the long-term transition from an analysis tool into an automation platform.

---

# 18. Key Product Principle

The FlowPilot user experience should follow one central principle:

> **The user describes the process. FlowPilot explains what to automate, why, and how.**

The product should make automation discovery accessible to business users without requiring them to understand the underlying technical implementation.

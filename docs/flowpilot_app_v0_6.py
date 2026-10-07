import streamlit as st
import ollama
import re

# --------------------------------------------------
# FlowPilot v0.6
# --------------------------------------------------

st.set_page_config(
    page_title="FlowPilot",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ FlowPilot")
st.subheader("AI Business Process Automation Consultant")

st.write(
    "Describe a manual business process and FlowPilot will analyze it, "
    "identify automation opportunities, recommend AI agents, and calculate "
    "the automation potential."
)

# --------------------------------------------------
# Process Input
# --------------------------------------------------

process = st.text_area(
    "Describe your business process",
    height=220,
    placeholder=(
        "Example:\n"
        "When a new employee joins the company, HR receives the employee "
        "information by email, enters the data into Excel, creates an account "
        "in the HR system, sends onboarding documents, checks whether all "
        "documents were received, and notifies the IT team."
    )
)

# --------------------------------------------------
# Scoring Engine
# --------------------------------------------------

def calculate_score(process_text):
    """
    Estimate automation potential from process signals.

    The score is intentionally deterministic so the same process
    produces the same result even when the local LLM changes its output.
    """

    text = process_text.lower()

    # Strong signals of manual/repetitive work.
    manual_keywords = [
        "manual", "manually", "enter", "input", "copy", "paste",
        "send", "check", "review", "prepare", "notify", "collect",
        "update", "create", "request", "follow up", "follow-up",
        "receive", "receives"
    ]

    repetition_keywords = [
        "every", "each", "daily", "weekly", "monthly", "regularly",
        "repeated", "repetitive", "routine", "recurring", "multiple",
        "often", "new employee", "each employee", "follow up",
        "follow-up"
    ]

    rule_keywords = [
        "if", "when", "check", "verify", "validate", "match", "compare",
        "approve", "approval", "criteria", "according to", "required",
        "condition", "missing", "complete", "incomplete"
    ]

    error_keywords = [
        "error", "errors", "mistake", "mistakes", "incorrect", "missing",
        "duplicate", "duplicates", "delay", "delays", "risk",
        "data entry", "omission", "omissions"
    ]

    integration_keywords = [
        "email", "excel", "spreadsheet", "hr system", "crm", "erp",
        "database", "system", "software", "portal", "api", "it team",
        "account", "accounts", "employee record", "record"
    ]

    ai_keywords = [
        "read", "scan", "document", "documents", "extract", "classify",
        "summarize", "analyze", "generate", "categorize", "respond",
        "route", "information", "email", "verify", "review"
    ]

    def count_matches(keywords):
        return sum(1 for keyword in keywords if keyword in text)

    manual_hits = count_matches(manual_keywords)
    repetition_hits = count_matches(repetition_keywords)
    rule_hits = count_matches(rule_keywords)
    error_hits = count_matches(error_keywords)
    integration_hits = count_matches(integration_keywords)
    ai_hits = count_matches(ai_keywords)

    # Balanced scoring.
    manual_score = min(20, manual_hits * 2)
    repetition_score = min(20, repetition_hits * 4)
    rules_score = min(15, rule_hits * 3)
    error_score = min(15, error_hits * 3)
    integration_score = min(15, integration_hits * 3)
    ai_score = min(15, ai_hits * 2)

    raw_total = (
        manual_score
        + repetition_score
        + rules_score
        + error_score
        + integration_score
        + ai_score
    )

    # Normalize around the six scoring dimensions.
    total = min(100, raw_total)

    # Process-level signals that should materially increase the score.
    strong_automation_signals = [
        "employee record",
        "it account",
        "onboarding",
        "missing documents",
        "follow up",
        "follow-up",
        "document",
        "email"
    ]

    strong_signal_hits = sum(
        1 for signal in strong_automation_signals if signal in text
    )

    total = min(100, total + strong_signal_hits * 3)

    return {
        "manual": manual_score,
        "repetition": repetition_score,
        "rules": rules_score,
        "error": error_score,
        "integration": integration_score,
        "ai": ai_score,
        "total": total
    }


def get_score_explanation(scores, process_text):
    text = process_text.lower()
    reasons = []

    if scores["repetition"] >= 10:
        reasons.append("The process contains repeated or routine work.")

    if scores["integration"] >= 8:
        reasons.append("Multiple systems, records, accounts, or communication channels are involved.")

    if scores["rules"] >= 6:
        reasons.append("Several steps can be handled using rules, validation, or conditions.")

    if scores["ai"] >= 8:
        reasons.append("Documents, information, review, or communication create useful AI opportunities.")

    if scores["error"] >= 6:
        reasons.append("Automation could reduce missing information, errors, or delays.")

    if not reasons:
        reasons.append("The process contains some automatable work, but the available signals are limited.")

    return reasons


# --------------------------------------------------
# Analyze Button
# --------------------------------------------------

if st.button("🔍 Analyze Process", use_container_width=True):

    if not process.strip():

        st.warning("Please describe a business process first.")

    else:

        prompt = f"""
You are FlowPilot, an AI business-process automation consultant.

Analyze ONLY the process provided below.

PROCESS:
{process}

Be specific to the user's process.
Do not invent a different business process.

Return these sections:

PROCESS SUMMARY
Explain the actual process in 2-3 sentences.

REPETITIVE TASKS
List the repetitive manual tasks.

BOTTLENECKS
List the main delays, risks, and inefficiencies.

AUTOMATION OPPORTUNITIES
List concrete tasks that can be automated.

AI AGENTS
Suggest 2-4 AI agents specifically relevant to this process.
Explain what each agent would do.

AUTOMATION WORKFLOW
Create a realistic workflow with 5-8 numbered steps.
Each step must be unique.
Do not repeat steps.
Include decision or human approval points when appropriate.

IMPORTANT:
Do not calculate an automation score.
Do not output SCORE_MANUAL.
Do not output SCORE_REPETITION.
Do not output an overall score.
"""

        # --------------------------------------------------
        # Ollama Analysis
        # --------------------------------------------------

        with st.spinner("FlowPilot is analyzing the process..."):

            try:

                response = ollama.chat(
                    model="qwen2.5:0.5b",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                answer = response["message"]["content"]

            except Exception as e:

                st.error("Could not connect to Ollama.")
                st.code(str(e))
                st.stop()

        # --------------------------------------------------
        # Display Analysis
        # --------------------------------------------------

        st.divider()

        st.header("🧠 FlowPilot Analysis")

        st.markdown(answer)

        # --------------------------------------------------
        # Calculate Score
        # --------------------------------------------------

        scores = calculate_score(process)

        total_score = scores["total"]

        # --------------------------------------------------
        # Automation Potential
        # --------------------------------------------------

        st.divider()

        st.header("📊 Automation Potential")

        if total_score >= 70:

            level = "🟢 High Automation Potential"

        elif total_score >= 40:

            level = "🟡 Medium Automation Potential"

        else:

            level = "🔴 Low Automation Potential"

        st.subheader(level)

        st.progress(total_score / 100)

        st.metric(
            "Automation Score",
            f"{total_score}/100"
        )

        # --------------------------------------------------
        # Score Breakdown
        # --------------------------------------------------

        st.subheader("📐 Score Breakdown")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Manual Work",
                f"{scores['manual']}/20"
            )

            st.metric(
                "Repetition",
                f"{scores['repetition']}/20"
            )

        with col2:

            st.metric(
                "Rule-Based Decisions",
                f"{scores['rules']}/15"
            )

            st.metric(
                "Error Reduction",
                f"{scores['error']}/15"
            )

        with col3:

            st.metric(
                "System Integration",
                f"{scores['integration']}/15"
            )

            st.metric(
                "AI Suitability",
                f"{scores['ai']}/15"
            )

        st.caption(
            "The automation score is calculated by FlowPilot's deterministic "
            "scoring engine from signals in the process description."
        )

        # --------------------------------------------------
        # Why This Score?
        # --------------------------------------------------

        st.subheader("💡 Why This Score?")

        reasons = get_score_explanation(scores, process)

        for reason in reasons:
            st.write(f"• {reason}")

        # --------------------------------------------------
        # Human in the Loop
        # --------------------------------------------------

        st.divider()

        st.subheader("👤 Human-in-the-Loop")

        st.info(
            "High-risk decisions, approvals, exceptions, and sensitive "
            "business actions should remain subject to human review."
        )

        # --------------------------------------------------
        # Recommendation
        # --------------------------------------------------

        st.divider()

        st.subheader("🚀 Recommendation")

        if total_score >= 70:

            st.success(
                "This process is a strong candidate for automation. "
                "A hybrid workflow using AI agents, deterministic automation, "
                "system integrations, and human approval points could "
                "significantly reduce manual work."
            )

        elif total_score >= 40:

            st.warning(
                "This process has moderate automation potential. "
                "Start with the most repetitive and rule-based tasks, "
                "while keeping human review for important decisions."
            )

        else:

            st.info(
                "This process has limited automation potential. "
                "Start by automating the most repetitive and rule-based tasks."
            )

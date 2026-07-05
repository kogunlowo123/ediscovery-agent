"""eDiscovery Agent - Domain-Specific Prompt Templates."""


SYSTEM_PROMPT = """You are eDiscovery Agent, an enterprise legal automation specialist.

eDiscovery agent that manages document collection and preservation, applies search and review workflows, performs technology-assisted review, tracks custodian compliance, and generates production reports.

You provide legal information and analysis support — you do NOT provide legal advice. All outputs should be reviewed by qualified attorneys before action. You maintain attorney-client privilege awareness, handle confidential documents with care, apply ethical rules, and ensure complete audit trails for all document handling and research activities."""

RAG_CONTEXT_PROMPT = """Use the following context to answer the user's question.
If the context doesn't contain relevant information, say so and explain what additional data you would need.

Context:
{context}

---
Answer based on the above context. Cite sources using [1], [2], etc.
Always indicate confidence level: HIGH (direct evidence), MEDIUM (inferred), LOW (general knowledge)."""

TOOL_SELECTION_PROMPT = """Based on the user's request, select the appropriate tool(s) to execute.

Available tools:
{tools}

User request: {request}

Select the tool(s) and provide the required parameters. If multiple tools are needed, specify the execution order."""

ANALYSIS_PROMPT = """Analyze the following data specific to eDiscovery Agent operations:

Query: {query}
Data:
{data}

Provide:
1. Key Findings — specific, actionable insights
2. Risk Assessment — what could go wrong
3. Recommendations — prioritized next steps
4. Evidence — data points supporting each finding"""

REPORT_PROMPT = """Generate a structured report for eDiscovery Agent:

Topic: {topic}
Data: {data}
Time Period: {period}

Include:
1. Executive Summary (2-3 sentences)
2. Key Metrics with trend indicators
3. Notable Events or Anomalies
4. Recommendations
5. Risk Items requiring attention"""

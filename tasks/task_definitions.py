"""
Task Definitions for Research Crew

Defines the four sequential tasks:
1. Query Expansion - Break down the research question
2. Source Hunting - Search the paper corpus
3. Synthesis - Analyze and synthesize findings
4. Report Writing - Generate the literature review

Each task should:
- Have a clear description telling the agent what to do
- Specify the agent responsible
- Define expected_output format
- Use context parameter to pass information between tasks
"""

from crewai import Task

from agents import query_expander, report_writer, source_hunter, synthesizer


def create_research_tasks(research_question: str) -> list[Task]:
    """
    Create the task pipeline for a research question.

    Args:
        research_question: The user's research question

    Returns:
        List of 4 tasks in execution order

    """

    # =========================================
    # Task 1: Query Expansion
    # =========================================
    expand_task = Task(
        description=(
            f"Break down the research question: {research_question}\n"
            "Identify focused sub-questions, key concepts, keywords and synonyms, "
            "and complementary search angles. Formulate search queries for each "
            "sub-question to guide searching the paper corpus."
        ),
        agent=query_expander,
        expected_output=(
            "A structured research search strategy containing the original question, "
            "numbered sub-questions, keywords and synonyms, search angles, and "
            "concrete search queries mapped to each sub-question."
        ),
    )

    # =========================================
    # Task 2: Source Hunting
    # =========================================
    search_task = Task(
        description=(
            f"Search the curated paper corpus for evidence addressing: {research_question}\n"
            "Use search_papers with the query strategy from the query expansion task. "
            "Search each sub-question, varying keywords, synonyms, and search angles "
            "to find 8-12 distinct relevant passages, including supporting and "
            "contradictory findings. Preserve the returned source metadata, map each "
            "passage to the sub-question it addresses, and report gaps in corpus "
            "coverage without inventing evidence or citations."
        ),
        agent=source_hunter,
        context=[expand_task],
        expected_output=(
            "A structured evidence collection of 8-12 relevant passages, or fewer "
            "if the corpus lacks sufficient evidence. For each passage, include "
            "the passage text, available paper citation and source metadata, "
            "relevance score, related sub-question, and a brief explanation of "
            "its relevance. Summarize search queries used and any evidence gaps."
        ),
    )

    # =========================================
    # Task 3: Synthesis
    # =========================================
    #

    synthesis_task = Task(
        description=(
            f"Synthesize the findings for the research question: {research_question}\n"
            "Use the query strategy and retrieved sources to group findings into "
            "coherent themes. Compare agreements and contradictions across studies, "
            "evaluate the strength and limitations of the evidence, and identify "
            "research gaps. Connect each theme to the relevant sub-questions and "
            "cite the supporting sources without inventing findings or citations."
        ),
        agent=synthesizer,
        context=[expand_task, search_task],
        expected_output=(
            "A structured synthesis organized by theme, with key findings, supporting "
            "source citations, agreements and contradictions, evidence limitations, "
            "research gaps, and an overall answer to the research question."
        ),
    )

    # =========================================
    # Task 4: Report Writing
    # =========================================
    #

    report_task = Task(
        description=(
            f"Write the final literature review for the research question: {research_question}\n"
            "Use the synthesized findings, retrieved sources, and query strategy to "
            "compose a coherent and comprehensive literature review. Ensure that each "
            "claim is supported by the appropriate sources and that gaps in the evidence "
            "are clearly noted. Do not invent findings or citations."
        ),
        agent=report_writer,
        context=[expand_task, search_task, synthesis_task],
        expected_output=(
            "A well-structured literature review that addresses the research question, "
            "organized by themes, with proper citations, discussion of agreements and "
            "contradictions, evidence limitations, research gaps, and a summary answer "
            "to the research question."
        ),
    )

    return [expand_task, search_task, synthesis_task, report_task]

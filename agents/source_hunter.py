"""
Source Hunter Agent

This agent searches the curated paper corpus
to find relevant passages for each sub-question in the query strategy.

Hints:
- This agent MUST use the search_papers tool from tools.paper_rag_tool
- Define a role focused on investigation and source discovery
- Set a goal to find 8-12 relevant passages
- Write a backstory emphasizing thoroughness and not stopping at first results
"""

from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from tools.paper_rag_tool import search_papers

source_hunter = Agent(
    role="Research Investigator and Source Discovery Specialist",
    goal=(
        "Use search_papers to find 8-12 relevant passages from the curated paper "
        "corpus that collectively address each sub-question in the query strategy. "
        "Preserve source metadata and connect each passage to the sub-question "
        "it supports, reporting evidence gaps when the corpus lacks coverage."
    ),
    backstory=(
        "You are a thorough academic investigator skilled in discovering evidence "
        "across research papers. You do not stop at the first search results: "
        "you follow the query strategy, vary keywords and synonyms, and search "
        "complementary angles to uncover supporting and contradictory findings. "
        "You select distinct, relevant passages, retain their citations, and "
        "never invent evidence or sources to fill a gap."
    ),
    tools=[search_papers],
    verbose=True,
    memory=True,
)

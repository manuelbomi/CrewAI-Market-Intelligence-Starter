"""CrewAI workflow for market intelligence.

This module defines a simple, production-friendly structure for a CrewAI workflow:
1. a tool that fetches stock data,
2. an agent that uses the tool,
3. a task for the agent to complete.
"""

from __future__ import annotations

from crewai import Agent, Crew, Process, Task
from crewai.tools import tool

from app.stock_tool import get_stock_data


@tool("get_stock_data")
def stock_tool(ticker: str) -> str:
    """Expose the stock data helper to CrewAI as a tool."""
    return get_stock_data(ticker)


def build_crew(ticker: str = "AAPL") -> Crew:
    """Create and configure the CrewAI workflow.

    Parameters
    ----------
    ticker:
        Default ticker requested by the workflow.

    Returns
    -------
    Crew
        A configured CrewAI crew instance.
    """
    researcher = Agent(
        role="Market Intelligence Researcher",
        goal="Gather accurate market data for {ticker}",
        backstory=(
            "A seasoned market analyst who turns raw financial data into useful "
            "insights for decision-makers."
        ),
        tools=[stock_tool],
        allow_delegation=False,
        verbose=False,
    )

    research_task = Task(
        description=(
            f"Use the stock data tool to gather a concise market summary for {ticker}."
        ),
        expected_output="A concise market data summary.",
        agent=researcher,
    )

    return Crew(
        agents=[researcher],
        tasks=[research_task],
        process=Process.sequential,
        verbose=False,
    )


def run_workflow(ticker: str = "AAPL") -> str:
    """Run the workflow and return a plain-text result summary."""
    crew = build_crew(ticker)
    # The current example uses the tool directly for clarity and deterministic output.
    # In a more advanced production setup, you could replace this with a full crew kickoff.
    result = stock_tool.run(ticker)
    return result

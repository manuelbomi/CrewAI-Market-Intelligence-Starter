"""Entry point for the CrewAI market intelligence starter.

This script demonstrates a simple but production-minded workflow:
1. a stock data tool fetches real market data,
2. a CrewAI agent is configured to use that tool,
3. the workflow can be run from a single entry point.

The example is intentionally documented and structured so it can be extended to
real business scenarios such as LNG supply monitoring or financial advisory.
"""

from __future__ import annotations

from app.crew_workflow import run_workflow
from app.logging_utils import configure_logging
from config import SETTINGS


def main() -> None:
    """Run the workflow for a default ticker and print the result."""
    configure_logging()
    ticker = SETTINGS.ticker
    print(f"Running workflow for ticker: {ticker}")
    result = run_workflow(ticker)
    print(result)


if __name__ == "__main__":
    main()

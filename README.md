# CrewAI Market Intelligence Starter

This project is a production-minded starter for building CrewAI-based market intelligence workflows. It demonstrates how to:

- fetch live market data from Yahoo Finance,
- expose that data through a CrewAI tool,
- structure the project so it is easier to test and expand,
- configure runtime behavior through environment variables,
- add logging, retries, and in-memory caching,
- and prepare the codebase for GitHub use with Docker and CI support.

## What this project does

The current example uses a simple agent workflow to gather a market summary for a stock ticker such as AAPL. The code is intentionally organized so it can be extended into more advanced business workflows for market monitoring, advisory support, and operational planning.

## Key features

- Live market-data retrieval through Yahoo Finance
- CrewAI agent and tool integration
- Retry logic for transient network issues
- In-memory caching to reduce repeated lookups
- Centralized configuration through environment variables
- Logging for easier debugging and monitoring
- Basic regression testing
- Docker support for containerized execution
- GitHub Actions CI workflow for automated test runs

## Suggested production uses

1. LNG fuel stocking for a gas provider
   - Use the workflow to gather market signals for LNG-related companies, energy indices, and fuel-price proxies.
   - The system can help determine when inventory should be increased or reduced based on recent market conditions.
   - Example use: a gas provider monitors LNG-related market data and receives a daily summary to support procurement planning.
   - In a fuller deployment, this could be scheduled to run every morning and feed a dashboard or procurement alert system.

2. Financial advisory and planning
   - Use the workflow to collect concise company and market summaries for client portfolios.
   - Advisors can use it to support discussions around sector positioning, company fundamentals, and valuation context.
   - Example use: a financial planner runs a report for a client’s watchlist before a consultation.
   - With more development, this could become a client-facing briefing system with richer formatting and historical comparisons.

3. Market intelligence for internal operations
   - Use the workflow as a lightweight internal analyst for monitoring key tickers, sectors, or business-relevant market signals.
   - Example use: operations or strategy teams receive an automated summary before planning meetings.

## Project structure

- app/stock_tool.py — reusable stock-data access layer with retries and caching
- app/crew_workflow.py — CrewAI agent and task setup
- app/logging_utils.py — logging configuration helpers
- app/cache.py — simple in-memory cache implementation
- config.py — centralized runtime configuration
- tests/test_stock_tool.py — basic regression test
- main.py — simple entry point for the application
- Dockerfile — container build definition
- .github/workflows/ci.yml — GitHub Actions CI workflow

## Installation

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate  # Windows PowerShell
pip install -r requirements.txt
```

## Configuration

The application reads settings from environment variables with defaults. You can override them as needed.

```bash
$env:DEFAULT_TICKER="AAPL"
$env:DATA_TIMEOUT_SECONDS="15"
$env:LOG_LEVEL="INFO"
$env:USE_CACHE="true"
```

## Run the example

```bash
python main.py
```

## Run tests

```bash
pytest -q
```

## Run a daily report

You can generate a simple scheduled-style report for multiple tickers:

```bash
python daily_report.py
```

This is useful for daily monitoring, operations check-ins, or basic advisory brief generation.

## Run with Docker

```bash
docker build -t crewai-market-intelligence .
docker run --rm crewai-market-intelligence
```

## Production hardening checklist

This starter now includes several production-friendly improvements:

- modular code organization,
- a dedicated tool module for easier testing,
- retry logic for transient failures,
- in-memory caching to reduce repeated lookups,
- environment-based configuration,
- logging for debugging and monitoring,
- basic regression testing,
- Docker support for containerized execution,
- GitHub Actions CI for automated validation,
- and a structure that can be extended with scheduled jobs, databases, and richer reporting.

## Next steps for full production readiness

To move this closer to a fully production-ready system, consider adding:

- persistent caching or a database for historical results,
- a proper secrets-management approach,
- structured logging and alerting,
- rate limiting and provider failover,
- scheduled jobs or cron-based execution,
- richer reporting and dashboard integration,
- and deployment automation for cloud environments.

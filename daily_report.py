"""Generate a simple daily market intelligence report.

This script is meant to be run on a schedule (for example with cron, Task Scheduler,
or a cloud job runner). It uses the same stock tool and prints a report for one or more
symbols.
"""

from __future__ import annotations

from app.stock_tool import get_stock_data


def generate_report(tickers: list[str]) -> str:
    """Create a multi-line report for the given ticker symbols."""
    lines = ["Daily market intelligence report", "=" * 32]
    for ticker in tickers:
        lines.append(get_stock_data(ticker))
    return "\n".join(lines)


if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "NVDA"]
    print(generate_report(tickers))

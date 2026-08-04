"""Production-oriented stock data tool for the CrewAI example.

This module centralizes all stock-data access logic so the agent code can stay
simple and the behavior is easier to test and maintain.
"""

from __future__ import annotations

import logging
import time
from typing import Optional

import yfinance as yf

from app.cache import SimpleCache
from config import SETTINGS

logger = logging.getLogger(__name__)
_cache = SimpleCache(ttl_seconds=300)


def get_stock_data(ticker: str, *, timeout: int = 15) -> str:
    """Return a concise summary for a stock ticker.

    Parameters
    ----------
    ticker:
        Stock ticker symbol such as AAPL or LNG.
    timeout:
        Request timeout in seconds for the Yahoo Finance lookup.

    Returns
    -------
    str
        A human-readable summary string.
    """
    normalized_ticker = (ticker or "").strip().upper()
    if not normalized_ticker:
        return "Ticker is required."

    cached = _cache.get(normalized_ticker) if SETTINGS.use_cache else None
    if cached is not None:
        logger.info("Returning cached result for %s", normalized_ticker)
        return cached

    last_error: Optional[str] = None
    for attempt in range(3):
        try:
            logger.info("Fetching market data for %s (attempt %s)", normalized_ticker, attempt + 1)
            stock = yf.Ticker(normalized_ticker)
            info = stock.info
            price = info.get("regularMarketPrice", "n/a")
            market_cap = info.get("marketCap", "n/a")
            sector = info.get("sector", "n/a")
            currency = info.get("currency", "n/a")
            result = (
                f"{normalized_ticker}: price={price} {currency}, "
                f"marketCap={market_cap}, sector={sector}"
            )
            _cache.set(normalized_ticker, result)
            return result
        except Exception as exc:  # pragma: no cover - defensive fallback
            last_error = str(exc)
            logger.warning("Fetch failed for %s: %s", normalized_ticker, exc)
            time.sleep(1)

    return f"Unable to fetch data for {normalized_ticker}: {last_error}"

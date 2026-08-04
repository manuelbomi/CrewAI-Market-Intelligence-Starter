"""Application configuration for the market intelligence starter.

This module centralizes runtime settings so the app can be configured without
changing code. It uses environment variables with sensible defaults.
"""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Runtime settings loaded from environment variables."""

    ticker: str = os.getenv("DEFAULT_TICKER", "AAPL")
    timeout_seconds: int = int(os.getenv("DATA_TIMEOUT_SECONDS", "15"))
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    use_cache: bool = os.getenv("USE_CACHE", "false").lower() == "true"


SETTINGS = Settings()

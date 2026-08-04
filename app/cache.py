"""Simple in-memory caching helper for repeated lookups."""

from __future__ import annotations

from typing import Dict, Optional, Tuple


class SimpleCache:
    """A tiny cache that stores recent results in memory."""

    def __init__(self, ttl_seconds: int = 300) -> None:
        self.ttl_seconds = ttl_seconds
        self._store: Dict[str, Tuple[float, str]] = {}

    def get(self, key: str) -> Optional[str]:
        """Return a cached value if it is still fresh."""
        entry = self._store.get(key)
        if not entry:
            return None
        timestamp, value = entry
        import time

        if time.time() - timestamp > self.ttl_seconds:
            self._store.pop(key, None)
            return None
        return value

    def set(self, key: str, value: str) -> None:
        """Store a value in the cache."""
        import time

        self._store[key] = (time.time(), value)

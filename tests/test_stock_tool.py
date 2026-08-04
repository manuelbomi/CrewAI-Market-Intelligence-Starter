import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.stock_tool import get_stock_data


def test_get_stock_data_returns_summary():
    result = get_stock_data("AAPL")
    assert isinstance(result, str)
    assert "AAPL" in result

import json
from pathlib import Path

REPORT = Path("/app/report.json")


def _load():
    return json.loads(REPORT.read_text())


def test_report_is_valid_json():
    """Criterion 1: /app/report.json exists, is valid JSON, and has exactly the required keys."""
    assert REPORT.exists(), "no report.json found"
    assert REPORT.stat().st_size > 0, "report.json is empty"
    data = _load()
    assert set(data.keys()) == {"total_requests", "unique_ips", "top_path"}, (
        "report.json must contain exactly the keys total_requests, unique_ips, top_path"
    )


def test_total_requests():
    """Criterion 2: total_requests equals the number of non-empty log lines (6)."""
    value = _load()["total_requests"]
    assert isinstance(value, int) and value == 6


def test_unique_ips():
    """Criterion 3: unique_ips equals the count of distinct client IPs (3)."""
    value = _load()["unique_ips"]
    assert isinstance(value, int) and value == 3


def test_top_path():
    """Criterion 4: top_path is the single most-requested path (/index.html)."""
    assert _load()["top_path"] == "/index.html"
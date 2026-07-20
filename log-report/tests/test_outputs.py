"""Verifier for dynamo/log-report — one test per instruction.md success criterion."""

from __future__ import annotations

import json
from pathlib import Path

REPORT = Path("/app/report.json")

# Hand-checked against environment/access.log:
#   6 non-empty lines
#   3 distinct IPs: 192.168.0.1, 192.168.0.2, 10.0.0.5
#   paths: /index.html x3, /about.html x2, /api/login x1
EXPECTED_TOTAL = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATHS = frozenset({"/index.html"})


def _load_report() -> dict:
    return json.loads(REPORT.read_text(encoding="utf-8"))


def test_criterion_1_report_exists_and_is_valid_json():
    """instruction.md success criterion 1: /app/report.json exists and contains
    a single valid JSON object."""
    assert REPORT.is_file(), f"missing report at {REPORT}"
    payload = _load_report()
    assert isinstance(payload, dict), "report.json must be a JSON object"


def test_criterion_2_report_has_required_keys():
    """instruction.md success criterion 2: the object has the keys
    total_requests, unique_ips, and top_path."""
    payload = _load_report()
    for key in ("total_requests", "unique_ips", "top_path"):
        assert key in payload, f"missing required key: {key!r}"


def test_criterion_3_total_requests_correct():
    """instruction.md success criterion 3: total_requests equals the number
    of non-empty lines in /app/access.log."""
    payload = _load_report()
    assert payload["total_requests"] == EXPECTED_TOTAL, (
        f"total_requests expected {EXPECTED_TOTAL}, got {payload['total_requests']!r}"
    )


def test_criterion_4_unique_ips_correct():
    """instruction.md success criterion 4: unique_ips equals the number of
    distinct IP addresses across those lines."""
    payload = _load_report()
    assert payload["unique_ips"] == EXPECTED_UNIQUE_IPS, (
        f"unique_ips expected {EXPECTED_UNIQUE_IPS}, got {payload['unique_ips']!r}"
    )


def test_criterion_5_top_path_correct():
    """instruction.md success criterion 5: top_path equals the most-requested
    path in the log (or one of the tied top paths, if there is a tie)."""
    payload = _load_report()
    assert payload["top_path"] in EXPECTED_TOP_PATHS, (
        f"top_path expected one of {sorted(EXPECTED_TOP_PATHS)}, got {payload['top_path']!r}"
    )

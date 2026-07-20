#!/usr/bin/env python3
"""Oracle: build /app/report.json from /app/access.log."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

LOG_PATH = Path("/app/access.log")
OUT_PATH = Path("/app/report.json")
REQUEST_RE = re.compile(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ')


def main() -> None:
    ip_set: set[str] = set()
    path_counts: Counter[str] = Counter()
    total = 0

    for raw in LOG_PATH.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        total += 1
        ip_set.add(line.split(None, 1)[0])
        match = REQUEST_RE.search(line)
        if match:
            path_counts[match.group(1)] += 1

    if not path_counts:
        raise SystemExit("no request paths found in access.log")

    report = {
        "total_requests": total,
        "unique_ips": len(ip_set),
        "top_path": path_counts.most_common(1)[0][0],
    }
    OUT_PATH.write_text(json.dumps(report) + "\n", encoding="utf-8")
    print(f"wrote {OUT_PATH}")


if __name__ == "__main__":
    main()

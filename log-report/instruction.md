Parse the Apache-style access log at `/app/access.log` and write a JSON
summary to `/app/report.json`.

`/app/report.json` must be a single JSON object with exactly these keys:

- `total_requests` (integer): count of non-empty lines in `/app/access.log`.
- `unique_ips` (integer): count of distinct client IPs. The client IP is the
  first whitespace-separated field on each log line.
- `top_path` (string): the request path that appears most often. Extract the
  path from the quoted request (for example, from `"GET /index.html HTTP/1.1"`
  the path is `/index.html`). If two or more paths tie for the highest count,
  any one of the tied paths is acceptable.

## Success criteria

1. `/app/report.json` exists and contains a single valid JSON object.
2. The object has the keys `total_requests`, `unique_ips`, and `top_path`.
3. `total_requests` equals the number of non-empty lines in `/app/access.log`.
4. `unique_ips` equals the number of distinct IP addresses across those lines.
5. `top_path` equals the most-requested path in the log (or one of the tied
   top paths, if there is a tie).

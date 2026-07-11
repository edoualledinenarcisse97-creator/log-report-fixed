Read the Apache-style access log at `/app/access.log` and generate a JSON summary at `/app/report.json` containing the following keys:

- `total_requests` (int): number of non-empty request lines.
- `unique_ips` (int): number of distinct client IP addresses (first field of each line).
- `top_path` (string): the most frequently requested path, where a path is the request target in the request line. If two or more paths tie for the most requests, use the lexicographically smallest.

Success criteria:
1. `/app/report.json` exists and contains valid JSON.
2. `total_requests` equals the number of non-empty lines in the log.
3. `unique_ips` equals the count of distinct client IPs.
4. `top_path` is the most-requested path (ties broken by choosing the lexicographically smallest).
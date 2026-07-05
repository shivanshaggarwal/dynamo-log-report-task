You are given an Apache-style access.log file in the working directory.

## Your Task
Analyze the log file and generate a JSON summary with the following statistics:
- **total_requests**: Total number of log entries (lines)
- **unique_ips**: Number of unique client IP addresses
- **top_path**: The most frequently requested URL path (e.g., "/index.html")

## Output Format
Write your results to **/app/report.json** with exactly this structure:
```json
{
  "total_requests": <integer>,
  "unique_ips": <integer>,
  "top_path": "<string>"
}
import json
import re
from collections import Counter

def test_report_values():
    
    with open('/app/report.json') as f:
        data = json.load(f)
    
    
    with open('/app/access.log') as f:
        lines = f.readlines()
    
    
    expected_total = len(lines)
    expected_unique_ips = len(set(line.split()[0] for line in lines))
    
    
    path_pattern = re.compile(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ')
    paths = []
    for line in lines:
        match = path_pattern.search(line)
        if match:
            paths.append(match.group(1))
    
    expected_top_path = Counter(paths).most_common(1)[0][0] if paths else ""
    
   
    assert data['total_requests'] == expected_total, \
        f"total_requests: expected {expected_total}, got {data['total_requests']}"
    assert data['unique_ips'] == expected_unique_ips, \
        f"unique_ips: expected {expected_unique_ips}, got {data['unique_ips']}"
    assert data['top_path'] == expected_top_path, \
        f"top_path: expected {expected_top_path}, got {data['top_path']}"
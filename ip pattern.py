import re
ip_pattern=re.compile(r"\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}")
log_lines=["Request from 192.168.1.10","Blocked 10.0.0.5","OK 1.10.100.10067"]
for line in log_lines:
    match=ip_pattern.search(line)
 if match:
    print(match.gruop())

import re
line="2026-08-10 14:22:07 ERROR Disk usage above 90% on /dev/sdal"
pattern=r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)"
match=re.match(pattern,line)
if match:
    print("Timestamp:",match.group(1))
    print("Level:",match.group(2))
    print("Message:",match.group(3))

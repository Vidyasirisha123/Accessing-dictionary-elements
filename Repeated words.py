import re
text="This is is a sample sample test in in regex"
pattern=r"\b(\w+)\s+\1\b"
repeats=re.findall(pattern,text,flags=re.IGNORECASE)
print("Repeated words found:",repeats)

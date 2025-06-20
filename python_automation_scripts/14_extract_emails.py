import re

with open("emails.txt") as f:
    data = f.read()

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", data)
print("Found Emails:")
print("\n".join(set(emails)))
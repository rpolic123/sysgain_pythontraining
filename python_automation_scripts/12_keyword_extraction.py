import re
from collections import Counter

with open('article.txt') as f:
    words = re.findall(r'\w+', f.read().lower())

common = Counter(words).most_common(10)
for word, count in common:
    print(f"{word}: {count}")
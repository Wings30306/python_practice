import re
import collections

text = open('book.txt', encoding="utf8").read().lower()
words = re.findall(r'\w+', text)
print(collections.Counter(words).most_common(10))
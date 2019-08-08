# Import the regular expressions library
import re
# Import collections library to count words
import collections

"""
 Here we'll read everything into a string called text use the read() method.
Have it all in lowercase
"""
text = open("book.txt").read().lower()

"""
The pattern we're using is \w+
The w denotes anything that's not a whitespace, and the plus denotes one or more. So, for every
occurrence of one or more characters that are not whitespace, we view that as
a word. We may get some false positives - it's not perfect but it works fine for
"""
words = re.findall("\w+", text)

"""
Then, the counter() method from collections counts how many
occurrences there are and the most_common() method limits the results to ten
words
"""
print(collections.Counter(words).most_common(10))

# Write to files

# use r for read, w for write or a for append
f = open('newfile.txt', 'a')
lines = ['Hello','World','Welcome','To','File IO']
text = '\n'.join(lines)
f.writelines(text)
f.close()
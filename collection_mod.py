'''Python Quick Codes: Find the character with the maximum count in a sentence.
'''

import collections

sentence = "A quick yellow fox ran together a very large Python"

# Print a dictionary {letter: number of occurrences} including blank space.
print(collections.Counter(sentence))

# Print a list of five most common (letter, count) including blank space.
print(collections.Counter(sentence).most_common(5))

'''Python Quick Code to demonstrate:
1. Use of counter from inbuilt collection module of Python.
2. Function returning more than one value.
'''

from collections import Counter


def get_vowel_and_consonants(sentence):
    vowels = []
    consonants = []
    for i in sentence:
        if i in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(i)
        else:
            consonants.append(i)

    return vowels, consonants


sentence = "A quick brown fox jumps over the lazy dog"

# Tuple unpacking, more than two values from a return statement will be a tuple
vowels, consonants = get_vowel_and_consonants(sentence)

# Get occurrences of each alphabet. Counter returns a dictionary.
occurrences = Counter(sentence)

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Occurrences dictionary: {occurrences}")

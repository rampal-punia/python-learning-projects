from collections import Counter
import requests


def get_series(sentence):
    vowels = []
    consonants = []
    occurrences = Counter(sentence)
    for i in sentence:
        if i in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(i)
        else:
            consonants.append(i)

    return vowels, consonants, occurrences


sentence = "A quick brown fox jumps over the lazy dog"
my_series = get_series(sentence)
print(my_series[0])
print(my_series[1])
print(my_series[2])

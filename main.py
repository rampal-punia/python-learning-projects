from collections import Counter


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
series = get_series(sentence)
print(series[0])
print(series[1])
print(series[2])

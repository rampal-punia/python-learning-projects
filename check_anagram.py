'''Python Function: Check if two words are anagram. 
'''


def check_anagram(word1, word2):
    if sorted(word1.lower()) == sorted(word2.lower()):
        print(f"'{word1}' and '{word2}' are anagram.")
    else:
        print(f"'{word1}' and '{word2}' are not anagram.")


check_anagram("elbow", "below")
check_anagram("desserts", "stressed")
check_anagram("hello", "olhe")

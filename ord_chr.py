'''Python Project: Saving All Unicode Characters To A File |
Using ord() & chr() |
'''

lower_chars = "a quick brown fox jumps over the lazy dog"
upper_chars = lower_chars.upper()

chars_unicode = {chr(i) for i in range(111)}
print(chars_unicode)

#Practice Problems:

#Dictionary Questions:
# 1. Count the frequency of each character in a string using a dictionary.
s = "hello"
char_freq = {}
# for char in s:
#     char_freq[char] = char_freq.get(char, 0) + 1
# print(char_freq)
for char in s:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
print("Character Frequency:", char_freq)

# 2.Count the frequency of words in a sentence. 
sentence = "This is a test. This test is only a test."
words = sentence.split()
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print("Word Frequency:", word_freq)

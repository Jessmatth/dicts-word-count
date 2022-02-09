'''opens a file and counts how many times each space-separated word occurs in that file'''
from collections import Counter


with open("test.txt") as f:
    lines = f.readlines()

counter = Counter()
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for line in lines:
    words_lst = line.lower().split(" ")
    for word in words_lst:
        for char in word:
            if char in punc:
                word = word.replace(char, "")
        counter[word] += 1

print('counter', counter)

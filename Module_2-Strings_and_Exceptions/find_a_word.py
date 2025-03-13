"""
Lab Exercise 5 - Find A Word

We will give you two strings: one being a word(e.g, "dog")
and the second being a combination of any characters.

Your task is to write a program which answers the following question:
are the characters comprising the first string hidden inside the second string?

For example:
if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
if the second string is "vcxzxdcybfdstbywuefsas",
the answer is no (as the letters "d", "o", or "g" don't appear in this order)

Hints:
you should use the two-argument variants of the pos()
functions inside your code and don't worry about case sensitivity.
"""

word = input("Enter word: ").lower()
comb_chars = input("Enter combination of any characters: ").lower()

for char in word:
    if char == word[0]:
        word_index = comb_chars.find(char)
    else:
        word_index = comb_chars.find(char, word_index)

if word_index == -1:
    print("No")
else:
    print("Yes")

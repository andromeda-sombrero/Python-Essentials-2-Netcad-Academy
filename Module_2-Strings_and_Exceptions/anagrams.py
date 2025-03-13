"""
Lab Exercise 3 - Anagrams

An anagram is a new word formed by rearranging the letters of a word,
using all the original letters exactly once.
For example, the phrases "rail safety" and "fairy tales" are anagrams,
while "I am" and "You are" are not.

Your task is to write a program which:

asks the user for two separate texts;
checks whether, the entered texts are anagrams and prints the result.

Note:
assume that two empty strings are not anagrams;
treat uppercase and lowercase letters as equal;
spaces are not taken into account during the check – treat them as non-existent
"""

text = input("Enter two words: ").split(" ")

if len(text) > 1 and len(text) <= 2:
    first_word = sorted(text[0].lower())
    second_word = sorted(text[1].lower())

    if first_word == second_word:
        print("Anagrams")
    else:
        print("Not anagrams")
else:
    print("Please enter two words.")

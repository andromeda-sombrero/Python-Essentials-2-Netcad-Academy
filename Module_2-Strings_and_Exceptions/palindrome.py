"""
Lab Exercise 2 - Palindrome

palindrome - It's a word which look the same when read forward and backward.

Your task is to write a program which:
asks the user for some text;
checks whether the entered text is a palindrome, and prints the result.

Note:
assume that an empty string isn't a palindrome.
treat upper-case and lower-case letters as equal.
spaces are not taken into account during the check, treat them as non-existent.
"""

word = input("Enter a phrase: ").lower()
word = word.split(" ")
word = "".join(word)
new_word = word[::-1]

if word == new_word:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")

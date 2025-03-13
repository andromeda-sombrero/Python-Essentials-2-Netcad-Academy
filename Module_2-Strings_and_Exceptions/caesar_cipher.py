"""
Lab Exercise 1 - Improving the Caesar Cipher.

Your task is to write a program which:
asks the user for one line of text to encrypt;
asks the user for a shift value (an integer number from the range 1..25
note: you should force the user to enter a valid shift value
(don't give up and don't let bad data fool you!)
prints out the encoded text.
"""

shift_value = 0
UPPERCASE_Z = 90
LOWERCASE_Z = 122
ALPHABET_NUM = 26

msg = input("Enter message to encrypt\nMessage: ")

while shift_value == 0:
    try:
        shift_value = int(input("Enter a shift value from range 1 to 25: "))
        if shift_value not in range(1, 26):
            raise ValueError
    except:
        shift_value = 0
        print("Please enter a valid number!")
    if shift_value == 0:
        print("Incorrect shift value!")

if shift_value != 0:
    new_msg = ""

    for ch in msg:
        if ch.isalpha():
            if ch.islower():
                if ord(ch) + shift_value > LOWERCASE_Z:
                    new_msg += chr(ord(ch) + shift_value - ALPHABET_NUM)
                else:
                    new_msg += chr(ord(ch) + shift_value)

            if ch.isupper():
                if ord(ch) + shift_value > UPPERCASE_Z:
                    new_msg += chr(ord(ch) + shift_value - ALPHABET_NUM)
                else:
                    new_msg += chr(ord(ch) + shift_value)
        else:
            new_msg += ch

    print(new_msg)

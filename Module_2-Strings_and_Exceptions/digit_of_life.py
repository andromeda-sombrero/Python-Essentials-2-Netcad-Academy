"""
Lab Exercise 4 - The Digit of Life

The Digit of Life - is a digit evaluated using somebody's birthday.
It's simple: you just need to sum all the digits of the date.

Your task is to write a program which: asks the user her/his birthday
(in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY actually) and
outputs the Digit of Life for the date.
"""

dob = input("Enter your date of birth: ").replace(" ", "")
total = 0

while len(dob) != 1:
    for ch in dob:
        total += int(ch)
    dob = str(total)
    total = 0

print(dob)

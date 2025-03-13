"""
Lab Exercise 7 - Reading Ints Safely

Your task is to write a function able to input integer values and to check
if they are within a specified range.

The function should:
1. Accept three arguments: a prompt, a low acceptable limit, and a high
acceptable limit;

2. If the user enters a string that is not an integer value, the function should
emit the message Error: wrong input, and ask the user to input the value again;

3. If the user enters a number which falls outside the specified range, the
function should emit the message Error: the value is not within permitted range
(min..max) and ask the user to input the value again;

4. If the input value is valid, return it as a result.
"""


def read_int(prompt, min_num, max_num):
    while True:
        try:
            num = int(input(prompt))
            if num < min_num or num > max_num:
                raise AssertionError
            return num

        except ValueError:
            print("Error: wrong input")

        except AssertionError:
            print("Error: the value is not within permitted range (-10..10)")


v = read_int(f"Enter a number between -10 to 10: ", -10, 10)

print(f"The number is: {v}")

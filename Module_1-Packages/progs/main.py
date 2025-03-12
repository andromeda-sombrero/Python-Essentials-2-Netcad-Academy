from sys import path

path.append("..\\modules")

from module import sum1, prod1

zeroes = [i + 1 for i in range(5)]
ones = [i + 1 for i in range(5)]
print(sum1(zeroes))
print(prod1(ones))

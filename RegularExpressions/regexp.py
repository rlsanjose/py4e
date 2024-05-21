import re

file = input("Write a file ")
fh = open(file, "r")
strings = re.findall('[0-9]+', fh.read())
sumOfNums = None
for number in strings :
    x = int(number)
    if sumOfNums is None :
        sumOfNums = x
    else :
        sumOfNums = sumOfNums + x
print(sumOfNums)

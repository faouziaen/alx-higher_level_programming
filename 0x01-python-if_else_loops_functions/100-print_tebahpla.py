#!/usr/bin/python3
result = ""
for i in range(ord('z'), ord('a') - 1, -1):
    result += "{:c}".format(i if i % 2 == 0 else i - 32)
print(result)

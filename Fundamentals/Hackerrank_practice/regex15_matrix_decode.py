#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
max_len = 0
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

max_len = max(len(word) for word in matrix)

final = []
for i in range(max_len):
    for j in matrix:
        final.append(j[i])
f1 = "".join(final)

pattern = re.sub(r'(?<=[a-zA-Z0-9])([!|@|#|$|%|&| ]+)(?=[a-zA-Z0-9])',' ', f1)
print(pattern)


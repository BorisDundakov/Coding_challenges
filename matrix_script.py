# Matrix script
# https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=true

import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

final_answer = ''
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

gc = ''
reg = re.compile("^[A-Za-z0-9_.]+$")
for col in range(m):
    for row in range(len(matrix)):
        try:
            tested = reg.match(matrix[row][col]).string
            for el in gc:
                final_answer += ' '
                break

            gc = ''
            final_answer += tested
        except AttributeError:
            gc += matrix[row][col]

    final_answer += gc

print(final_answer)

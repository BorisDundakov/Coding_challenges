# You are given a string S.
# Your task is to find out whether S is a valid regex or not.

# Input Format

# The first line contains integer
# , the number of test cases.
# The next lines contains the string

# Constraints

# Output Format

# Print "True" or "False" for each test case without quotes.

# Sample Input

# 2
# .*\+
# .*+

# Sample Output

# True
# False

# Explanation

# .*\+ : Valid regex.
# .*+: Has the error multiple repeat. Hence, it is invalid.

#SyntaxError: '(' was never closed [python]
#ERROR: Unable to parse file: incorrect_regex_2.py
#ERROR: Parse error at line 35 column 0: .... --> WARN: Unable to analyze file: incorrect_regex_2.py

print('Should return error'
      
import re


def check_regex(expression):
    try:
        re.compile(expression)
        print(True)
    except re.error:
        print(False)


t = int(input())
for x in range(t):
    s = input()
    check_regex(s)

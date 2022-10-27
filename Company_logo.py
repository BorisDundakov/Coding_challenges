#!/bin/python3

""""A newly opened multinational brand has decided to base their company logo on the three
most common characters in the company name. They are now trying out various combinations of company names
and logos based on this condition.

Given a string, which is the company name in lowercase letters, your task is to find the top
three most common characters in the string:
- Print the three most common characters along with their occurrence count.
- Sort in descending order of occurrence count.
- If the occurrence count is the same, sort the characters in alphabetical order.

For example, according to the conditions described above, 'GOOGLE'
would have its logo with the letters 'G', 'O', 'E'.

Input Format

A single line of input containing the string.

Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input:
aabbbccde

Sample Output:

b 3
a 2
c 2

Explanation:
Here, b occurs 3 times. It is printed first.
Both 'a' and 'c' occur 2 times. So, 'a' is printed in the second line and 'c' in the third line
because 'a' comes before 'c' in the alphabet.

Note: The string 's' has at least 3 distinct characters."""

s = 'aabbbccde'
letters = [0] * 256
for letter in s:
    letters[ord(letter)] += 1

ans = {}
for x in range(3):
    max_item = max(letters)
    max_idx = letters.index(max_item)
    ans[chr(max_idx)] = max_item
    letters[max_idx] = 0

for key, value in ans.items():
    print(f'{key} {value}')

"""In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.

Output Format:
Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input:
ABCDCDC
CDC

Sample Output:
2
"""


def count_substring(string, sub_string):
    res = 0
    if string.find(sub_string) == -1:
        return res
    start_idx = 0
    end_idx = len(string)
    while start_idx < end_idx:
        path = string[start_idx:len(sub_string)+start_idx]
        if path == sub_string:
            res += 1
        start_idx += 1
    return res


string = 'ABCDCDC'
sub_string = 'CDC'

count = count_substring(string, sub_string)
print(count)

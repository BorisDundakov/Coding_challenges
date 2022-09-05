"""you are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase
 letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

Sample Input:
HackerRank.com presents "Pythonist 2".

Sample Output:
hACKERrANK.COM PRESENTS "pYTHONIST 2"."""


# DAY 1 -> 04.09.22

def swap_case(s):
    list_swapped = [each_letter.upper() if each_letter.islower() else each_letter.lower() for each_letter in s]
    string_swapped = ''.join(list_swapped)
    return string_swapped


swap_case('sEriOUS ExamPLe')
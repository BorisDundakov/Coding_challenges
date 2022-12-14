"""There are 1.py disjoint sets, A and B.
You like all the integers in set A and dislike all the integers in set B.
Your initial happiness is 0. For each i integer in the array, if 'i' is in A,
you add 1 to your happiness. If 'i' is in B, you add -1 to your happiness.
Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

Output a single integer, your total happiness.

Sample Input:
1 5 3
3 1
5 7

Sample Output:
1

Explanation

You gain 1 unit of happiness for elements 3 and 1 in set A. You lose 1 unit for 5 in set B.
The element 7 in set B does not exist in the array, so it is not included in the calculation.

Hence, the total happiness is 1.py - 1 = 1."""

# DAY 1.py -> 05.09.22

happiness = 0

working_array = input().split()
A = set(input().split())
B = set(input().split())

bombastic = 0
bombastic = sum([bombastic + 1 if current_number in A else bombastic - 1 for current_number in working_array])
print(bombastic)

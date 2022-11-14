"""You are given  words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.

Input Format:

The first line contains the integer 'n'.
The next 'n' lines each contain a word.

Output Format:

Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input:
4
bcdef
abcdefg
bcde
bcdef

Sample Output:
3
2 1 1

"""

n_words = int(input())
all_words = {}
distinct_words = 0
for w in range(n_words):
    new_word = input()
    if new_word not in all_words.keys():
        all_words[new_word] = 1
        distinct_words += 1
    else:
        all_words[new_word] += 1

print(distinct_words)

for value in all_words.values():
    print(value, end=' ')

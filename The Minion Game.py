# DAY 3 -> 08.09.22

"""Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 1.py Points."""


def minion_game(string):
    stuart_points = 0
    kevin_points = 0
    for i in range(0, len(string)):
        if string[i] not in ('A', 'E', 'I', 'O', 'U'):
            stuart_points = stuart_points + len(string) - i
        else:
            kevin_points = kevin_points + len(string) - i
    if stuart_points > kevin_points:
        print("Stuart", stuart_points)
    elif kevin_points > stuart_points:
        print("Kevin", kevin_points)
    else:
        print("Draw")


minion_game('HANNIBAL')

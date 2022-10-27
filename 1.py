"""
This problem was asked by Facebook.
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string ([])[]({}), you should return true.
Given the string ([)] or (((), you should return false."""


# count -> ( === count -> )
# count -> [ === count -> ]
# count -> { === count -> }


def even_brackets(brackets):
    if brackets[0] not in ['{', '(', '[']:
        return False

    answ = {'(': 0, ')': 0, '[': 0, ']': 0, '{': 0, '}': 0}
    for el in brackets:
        answ[el] += 1

    if answ['('] != answ[')']:
        return False
    if answ['{'] != answ['}']:
        return False
    if answ['['] != answ[']']:
        return False
    return True


print(even_brackets(')([])[]({})('))

'''''Given the names and grades for each student in a class of N

students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0

Berry
Harry

'''


if __name__ == '__main__':
    records = []
    result = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    records.sort(key=lambda x: (x[1], x[0]))
    records.reverse()
    lowest_entry = (records.pop())
    lowest_score = lowest_entry[1]

    for x in reversed(records):
        if x[1] == lowest_score:
            continue
        if not result:
            result.append(x)
        elif x[1] == result[0][1]:
            result.append(x)
        else:
            break

    [print(name[0]) for name in result]

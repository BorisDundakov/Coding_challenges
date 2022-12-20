#The National University conducts an examination of 'N' students in 'X' subjects.
#Your task is to compute the average scores of each student

n_marks, n_students = input().split()

marks = []
for mark in range(int(n_students)):
    marks.append([float(el) for el in input().split()])

for el in range(int(n_marks)):
    avg = 0
    idxs = []
    for z in range(int(n_students)):
        idxs.append(z)
    for c_idx in range(len(idxs)):
        avg += marks[c_idx][el]

    avg = avg / int(n_students)
    print(avg)

from ast import Delete


StudentAmount = int(input())
# StudentAmount = 5

Students = []
for i in range(StudentAmount):
    a,b = map(int,input().split())
    Students.append([a,b])

# StudentRanks = [[0] for i in range(StudentAmount)]

# print(Students)

for Student1 in Students:
    rank =1
    for Student2 in Students:
        if Student1[0]<Student2[0] and Student1[1]<Student2[1]:
            rank+=1
    print(rank, end = ' ')
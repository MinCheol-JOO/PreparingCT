st_count = int(input())

student = []
for _ in range(st_count):
    name,age = input().split()
    student.append([name,age])


array = sorted(student,key = lambda student : student[1])
for i in array:
    print(i[0])
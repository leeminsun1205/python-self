n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores 
query_name = input()
s = 0
for i in range(3):
    s += student_marks[query_name][i]
aver = s / 3
print('%.2f' % aver)
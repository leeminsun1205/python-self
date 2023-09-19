# a = range(1, 10, 1)
# a = range(1, 10)
# for i in a:
#     print(i, end = ' ')
for i in range(0, 51, 2):
    print(i, end = ' ')  
    print('Le Minh Nhut')  
n = int(input('Nhap so n: '))
s = 0
for i in range(1, n + 1):
    s += i ** 2
print(s)
for i in range(1, 7):
    print(i)
    i += 100
else:
    print('Vong for da ket thuc!')
for i in range (1, 21):
    print(i, end = ' ')
    if i % 7 == 0:
        break
    print('Cau lenh ben duoi break')
for i in range(3):
    for j in range(2):
        print(i, j)
n = 100
for i in range(1, 101):
    if n % i == 0:
        print(i, end = ' ')
a, b = map(int, input('Nhap 2 so nguyen bat ki: ').split())
if a > b and a < 100:
    print('Le Minh Nhut dep trai')
    print('Haha')
print('LaLa')
if a % 2 == 0:
    print('Chan')
    print('Nhut dep trai')
else:
    print('Le')
if a < b:
    print(a, 'less than', b)
elif a > b:
    print(a, 'greater than', b)
else:
    print(a, 'equal to', b)
t = int(input('Nhap thang can tim:'))
if t == 1 or t == 3 or t == 5 or t == 7 or t == 8 or t == 10 or t == 12:
    print('Thang co 31 ngay\n')
elif t == 4 or t == 6 or t == 9 or t == 11:
    print('Thang co 30 ngay\n')
elif t == 2:
    print('Thang co 28 hoac 29 ngay\n')
else:
    print('Du lieu khong hop le!\n')
# Shorthand  if: Su dung cau lenh if tren 1 dong
if a < b: print(a, 'less than', b)
# Toan tu ba ngoi:
# variable = statement if condition else statement
res = 'a less than b' if a < b else 'a greater than b'
print(res)
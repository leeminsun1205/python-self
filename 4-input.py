s = int(input('Xin nhap du lieu tu ban phim: ')) 
print('Du lieu vua nhap la:', s)
print(type(s))
a = int(input('Nhap chieu dai: '))
b = int(input('Nhap chieu rong: '))
chuvi = 2 * (a + b)
dientich = a * b
print(chuvi, dientich)
'''
s1 = input('Nhap 3 so: ')
a1 = s1.split()
x, y, z = a1
print(x + y + z)
x, y, z = map(int, a1)
print(x + y + z)
'''
x, y, z, t = map(int, input('Nhap 4 so nguyen: ').split())
print(x, y, z ,t)
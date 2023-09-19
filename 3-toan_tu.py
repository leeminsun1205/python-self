a, b, c = 100, 200, 'ab'
print(a, b, c)
a, b = b, a
print(a, b, c)
d = b + 50 - a * 10
k = 100 / 40
e = 100 // 30
f = 7 % 2
m = -2 ** 3
print(m, d, e, f, k)
print(100 != 100)
print((10 == 10) and (2 >=1))
print(not 10)
print(2 or 0)
l = [1, 2, 3]
n = [1, 2, 3]
print(id(l))
print(id(n))
print(l == n)
print(l is n)
s = 'Minh la Le Minh Nhut o Ben Tre hoc tai UIT'
print('Le Minh Nhut' in s)
print('Le Minh nhut' not in s)
dai = 100.56
rong = 50.23
chu_vi = 2 * (dai + rong)
dien_tich = dai * rong
print('Chu vi la:', '%.2f' % chu_vi, '\nDien tich la:', '%.2f' % dien_tich)
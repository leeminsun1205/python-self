n = 1
while n <= 5:
    print('Vong lap tuong ung khi n =', n)
    n += 1
else:
    print('Vong lap while ket thuc khi n =', n)
while 1:
    n = int(input())
    if n > 0: break
m = int(input('Nhap m:'))
# dem = 0
# while m != 0:
#     m //= 10
#     dem += 1 
# else: dem = 1
# print(dem)
lat = 0
while m != 0:
    lat = lat * 10 + m % 10
    m //= 10
print(lat)
    
    
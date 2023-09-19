a = [1, 2, 3, 4, 4, 3 , 1, 2]
#dem so lan xuat hien cua 1 phan tu
c = a.count(4)
#tra ve vi tri dau tien xuat hien cua phan tu trong chuoi
c = a.index(4)
#copy
c = a.copy() # co tac dung giong list constructor
c[0] = 'Nhut'
#clear
c = a.clear()
print(c)
print(a)
A = [1, 2, 3]
B = A.copy()
A.append([4, 5])
B.extend([4, 5, [4, 5]])
print(A)
print(B)
A.insert(4, 9)
print(A)
C = A.pop(1)
print(A)
print(C)
D = [1, 1, 2, 3, 4, 4]
D.reverse()
print(D)
D.remove(1)
D.remove(1)
print(D)
E = [4, 1, 6, 2, 5, 3]
print(E)
E.sort(reverse=True)
print(E)

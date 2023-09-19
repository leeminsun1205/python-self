# giới hạn bởi cặp ngoặc vuông []
# các phần tử của list cách nhau bởi dấu ,
# list có khả năng chứa mọi giá trị đối tượng của python 
# và bao gồm chính nó
a = [1, 2, 5, 'Minh Nhut']
b = [[1, 2, 3], [4, 5, 6], ['Minh Nhut', 'Tuyet An', 'Phuong Thao']]
c = [i for i in range(2, 30, 2)]
d = [[n, n * 2, n *3] for n in range(1, 4)]
e = list('Kteam')
a += ['one', 'two', 'five']
a *= 2
f = 1 in a
g = [1, 2, 'a', 'b', 'c', [3, 4]]
h = g[5][0]
g[1] = 'Nhut'
print(a)
# print(b)
# print(c)
print(d)
# print(e)
print(g)
print(f)
print(h)
#tiếp
A = [1, 2, 3]
B = A
B = list(A)
B[0] = '100'
print(A)
print(B)

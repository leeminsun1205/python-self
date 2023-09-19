#function
def tong(a, b):
    res = a + b
    return res
m, n= 12, 5
print(tong(m, n))
def xinchao(name1, name2, name3):
    print('Xin chao', name1, name2, name3)

xinchao('Teo', 'Ty', 'Nam')
#code để chạy chương trình
if __name__ == '__main__':
    x, y = map(int, input().split())
    print(tong(x, y))
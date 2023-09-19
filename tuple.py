#được giới hạn bởi cặp ngoặc tròn
#các phần tử của tuple được phần cách nhau bởi dấu ,
#tuple có khả năng chứa mọi giá trị 
#tốc độ truyy xuất tuple nhanh hơn list*
#dung lượng chiếm trong bộ nhớ nhỏ hơn list
#bảo vệ dữ liệu của bạn sẽ không bị thay đổi*
#có thể dùng làm key của dictionary
tup1 = (1, 1, 2, (5, 6, 7), 'Nhut', 'An')
print(tup1)
#trường hợp không tính là tuple
tup = (1)
tup = (i for i in range(10) if i % 2 == 0)
a = tuple(tup)
print(a)
tup1 += (1, 2, 3)
print(tup1)
b = tup1[::-1]
print(b)
#Các phương thức tương tự
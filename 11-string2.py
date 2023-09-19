#Chuoi tran chi can them r truoc chuoi se khong quan toi cac ki hieu
print(r'Haizz, \neu mot ngay nao do')
strA = 'Le Minh Nhut\n'
strB = 'Le'
#cong chuoi
strC = strA + strB
print(strC)
#nhan chuoi
strD = strA * 5
print(strD)
#in: kiem tra xem 1 chuoi co nam trong 1 chuoi khac hay khong
strE = strB in strA
print(strE)
print(strC[-4])
print(len(strC))
strF = strA[3:None]
strG = strA[3:len(strA)]
strG1 = strA[None:None:-1]
strH = strA[None:None]
print(strF)
print(strG1)
A = int("69") + 5
B = int(6.9)
C = str(69) + "5"
print(A)
print(B)
print(C)
strA = strA[None:1] + "0" + strA[2:None]
print(hash(strA))
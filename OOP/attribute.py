class SieuNhan:
    suc_manh = 50
    stt = 0
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = 'Sieu nhan' + ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
        SieuNhan.stt += 1
        self.stt = SieuNhan.stt
    def xin_chao(self):
        print("Xin chao, ta la", self.ten)
        print("Suc manh cua ta la", self.suc_manh)
    
SN_A = SieuNhan("Tim", "Cute", "Tim khoai mon")
SN_B = SieuNhan("Den", "Tinh yeu", "Den huyen bi")
SN_C = SieuNhan("Do", "Manh me", "Do loet")

SN_A.suc_manh = 40
print(SN_A.suc_manh)
print(SieuNhan.suc_manh)

print(SN_A.stt)
print(SN_B.stt)
print(SN_C.stt)

SN_A.xin_chao()
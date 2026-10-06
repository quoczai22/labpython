class WordPlay:
    def __init__(self):
        self.ds_tu = []
        
    def input_info(self):
        ds_tu = input("Hay nhap danh sach chu tach nhau boi space: ")
        self.ds_tu = ds_tu.split()
        
    def words_with_length(self, length):
        ket_qua = []
        for tu in self.ds_tu:
            if len(tu) == length:
                ket_qua.append(tu)
        return ket_qua
    
    def started_with_s(self, s):
        ket_qua = []
        for tu in self.ds_tu:
            if tu.startswith(s):
                ket_qua.append(tu)
        return ket_qua
    
    def end_with_s(self, s):
        ket_qua = []
        for tu in self.ds_tu:
            if tu.endswith(s):
                ket_qua.append(tu)
        return ket_qua
    
    def only_L(self, L):
        ket_qua = []
        for tu in self.ds_tu:
            gia_tri = True
            for chu in tu:
                if chu not in L:
                    gia_tri = False
                    break
            if gia_tri is True:
                ket_qua.append(tu)
        return ket_qua
    
    def avoids_L(self, L):
        ket_qua = []
        for tu in self.ds_tu:
            gia_tri = True
            for chu in tu:
                if chu in L:
                    gia_tri = False
                    break
            if gia_tri is True:
                ket_qua.append(tu)
        return ket_qua
    
    def display(self, tieu_de, danh_sach_ket_qua):

        if len(danh_sach_ket_qua) == 0:
            print("   (Không tìm thấy từ nào thỏa mãn)")
        else:
            print(f"   Kết quả: {', '.join(danh_sach_ket_qua)}")


def main():
    ds_tu1 = WordPlay()
    ds_tu1.input_info()
    

    kq_do_dai = ds_tu1.words_with_length(3)
    ds_tu1.display("Các từ có độ dài bằng 3", kq_do_dai)
    
    kq_bat_dau = ds_tu1.started_with_s("a")
    ds_tu1.display("Các từ bắt đầu bằng chữ 'a'", kq_bat_dau)
    
    kq_ket_thuc = ds_tu1.end_with_s("t")
    ds_tu1.display("Các từ kết thúc bằng chữ 't'", kq_ket_thuc)
    
    kq_only = ds_tu1.only_L("abn")
    ds_tu1.display("Các từ chỉ chứa ký tự thuộc 'abn'", kq_only)
    
    kq_avoids = ds_tu1.avoids_L("ei")
    ds_tu1.display("Các từ KHÔNG chứa ký tự 'e' hoặc 'i'", kq_avoids)

if __name__ == "__main__":
    main()

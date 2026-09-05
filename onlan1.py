# bai1 câu 1 

def chuyensonguyenso(n): 
    return float(n), str(n)

#cau 2

def kiemtrachanle(n):
    if n%2==0:
        return True
    else:
        return False

#cau3

def phanloaituoi(n):
    if(n<12):
        return "Trẻ em"
    elif(n<18):
        return "Thiếu niên"
    else:
        return "Người lớn"

#cau4 

def solonnhattrong3so(a,b,c):
    return max(a,b,c)

#cau5

def namnhuan(n):
    if(n%4==0 and n%100!=0) or (n%400==0):
        return True
    else:
        return False
    
# bai 2 cau 1
#cach 1
def insotu1den10():
    for i in range(1,11):
        print(i)
#cach 2

# def insotu1den10():
#     n=1
#     for i in range (10):
#         print(n)
#         n+=1

#cau 2

def bangcuuchuong(n):
    for i in range (1,11):
        print(f"{n} x {i} = {n*i}")

#cau 3
def tongtu1denn(n):
    tong=0
    for i in range(1,n+1):
        tong=tong+i
    return tong

#cau4

def vetamgiacvuong(n):
    for i in range(1,n+1):
        print("*"*i)

#bai3 3 cau 1

def chuyenhotenthanhchuthuong1(n):
    return str.lower(n)

#cau 2

def demsoluongkytucotrongchuoi(n):
    dem=0
    for i in n:
        dem=dem+1
    return dem

def demsochusovasochucai(n):
    demsochuso=0
    demsochucai=0

    for i in n:
        if i.isdigit():
            demsochuso=demsochuso+1
        elif i.isalpha():
            demsochucai=demsochucai+1
        
    return demsochucai,demsochuso

#cau 3 Nhập vào một câu (nhiều từ), đếm số lần xuất hiện của mỗi từ trong câu.
def demsolanxuathiencuatu(n):
    tu=n.split()
    demtu={}

    for i in tu:
        if i in demtu:
            demtu[i]+=1
        else:
            demtu[i]=1
    return demtu

#tach tu và dem so lan xuat hien cua moi tu trong cau
def demsolanxuathiencuatu(n):
    tu=n.split()
    demtu={}

    for i in tu:
        if i in demtu:
            demtu[i]+=1
        else:
            demtu[i]=1
    return demtu

def demsotuxuathien(n):
    dstu=n.split()
    for i in set(dstu):
        print(f" tu {i} xuat hien {dstu.count(i)} lan")

# cau4
def kiemtrachuoidoiung(n):
    chuoi_chuan_hoa= n.lower().replace(" ","")

    if chuoi_chuan_hoa==chuoi_chuan_hoa[::-1]:
        return True
    else:
        return False

# phần 2  bai 4 câu 1 Nhập vào một danh sách các số dưới dạng chuỗi (cách nhau bởi khoảng trắng), chuyển đổi nó thành một List các số nguyên.

def chuyenchuoi_thanhlistso(n):
    listso=n.split()
    for i in range(len(listso)):
        listso[i]=int(listso[i])
    return listso

# cau2

def tinh_tong_va_max(n):
    a=sum(n)
    b=max(n)
    return a,b

#cau3 Nhập vào một List tên học sinh, sắp xếp và in ra danh sách theo thứ tự bảng chữ cái (Alphabet).

def sap_xep_ten(n):
    n.sort()
    return n

#cau4
def tbc(n):
    return sum(n)/len(n)

# cau5
def loaibotrunglap1(n):
    ds_songuyen=[]
    for i in n:
        if i not in ds_songuyen:
            ds_songuyen.append(i)
    return ds_songuyen

def loaibotrunglap2(n):
    return list(set(n))

def chuyenhoathanhthuong(n):
    return n.lower()

# cau6
def tron(a,b):
    return a+b

def sapxep(n):
    n.sort()
    return n

#bai 5 cau 1 Tạo một Set chứa 5 số nguyên. Viết code để thêm 1 phần tử mới và xóa 1 phần tử đã có.

def themvaoset(s,pt):
    s.add(pt)
    return s

def main():
    # n=int(input("Nhập số nguyên: "))

    # a,b= chuyensonguyenso(n)

    # print("Kết quả của số nguyên khi chuyển qua float là",a)
    # print("Kết quả của số nguyên khi chuyển qua string là",b)

    # n=int(input("Nhập số nguyên: "))
    # if kiemtrachanle(n):
    #     print("Số", n, "là số chẵn")
    # else:
    #     print("Số", n, "là số lẻ")

    # n= int(input("Nhập tuổi: "))
    # print("Bạn thuộc nhóm tuổi:", phanloaituoi(n))

    # a=int(input("Nhập số thứ nhất: "))
    # b=int(input("Nhập số thứ hai: "))
    # c=int(input("Nhập số thứ ba: "))
    # print("Số lớn nhất trong 3 số là:", solonnhattrong3so(a,b,c))

    # n=int(input("Nhập năm: "))
    # if namnhuan(n):
    #     print("Năm", n, "là năm nhuận")
    # else:
    #     print("Năm", n, "không phải là năm nhuận")

    # insotu1den10()


    # n=int(input("Nhập số nguyên: "))
    # bangcuuchuong(n)

    # n=int(input("Nhập số nguyên: "))
    # print("Tổng từ 1 đến", n, "là:", tongtu1denn(n))

    # n=int(input("Nhập chiều cao: "))
    # vetamgiacvuong(n)

    # n=str(input("Hãy nhập vào họ tên của bạn: "))
    # print("Họ tên chữ thường là: ",chuyenhotenthanhchuthuong1(n))

    # n=str(input("Hãy nhập vào chuỗi: "))
    # print("Số lượng ký tự có trong chuỗi: ",demsoluongkytucotrongchuoi(n))

    # a,b=demsochusovasochucai(n)
    # print("Số chữ số trong chuỗi là: ",b)
    # print("Số chữ cái trong chuỗi là: ",a)

    # n=str(input("Hãy nhập vào chuỗi: "))
    # print("Số lần xuất hiện của từ trong chuỗi là: ", demsolanxuathiencuatu(n))
    # print(f"Số lần xuất hiện của từ trong chuỗi là: ", demsotuxuathien(n))

    # n=str(input("Hãy nhập vào chuỗi: "))
    # if kiemtrachuoidoiung(n):
    #     print("Chuỗi đối xứng")
    # else:
    #     print("Chuỗi không đối xứng")

    # n=str(input("Hãy nhập vào chuỗi các số cách nhau bởi khoảng trắng: "))

    # tong_cac_so, max_so = tinh_tong_va_max(chuyenchuoi_thanhlistso(n))

    # print("Danh sách các số nguyên là: ", chuyenchuoi_thanhlistso(n))
    # print("Tổng các số là: ", tong_cac_so)
    # print("Số lớn nhất trong danh sách là: ", max_so)
    # print("Trung bình cộng của các số là: ", tbc(chuyenchuoi_thanhlistso(n)))

    # n=int(input("Hãy nhập số lượng sinh viên mà bạn muốn nhập: "))
    # dssv=[]

    # for i in range(n):
    #     ten_sv=str(input(f"Hãy nhập tên sinh viên thứ {i+1}: "))
    #     dssv.append(ten_sv)

    # print("Danh sách tên sinh viên sau khi sắp xếp là: ", sap_xep_ten(dssv))

    # n=int(input ("Hay nhap so luong mang: "))
    # mang=[]

    # for i in range(n):
    #     k=(input(f"Hay nhap gia tri thu {i+1}: "))
    #     mang.append(k)
    #     mang[i] = chuyenhoathanhthuong(mang[i])
    # print("Mảng sau khi loại bỏ phần tử trùng lặp là: ", loaibotrunglap1(mang))
    # print("Mảng sau khi loại bỏ phần tử trùng lặp là: ", loaibotrunglap2(mang))

    # n=int(input ("Hay nhap so luong mang 1: "))
    # mang1=[]

    # m=int(input ("Hay nhap so luong mang 2: "))
    # mang2=[]

    # for i in range(n):
    #     k=(input(f"Hay nhap gia tri thu {i+1} cua mang 1: "))
    #     mang1.append(k)

    # for i in range(m):
    #     k=(input(f"Hay nhap gia tri thu {i+1} cua mang 2: "))
    #     mang2.append(k)

    # print("Mảng sau khi trộn và sắp xếp là: ", sapxep(tron(mang1,mang2)))

    n=int(input ("Hay nhap so luong phan tu trong set: "))
    s=set()
    for i in range(n):
        k=(input(f"Hay nhap gia tri thu {i+1}: "))
        s.add(k)
    print ("Set sau khi thêm phần tử mới là: ", themvaoset(s,(input("Hay nhap gia tri can them vao set: "))))

if __name__=="__main__":
    main()
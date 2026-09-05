# câu 1 

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
    
# phan 2 cau 1
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

#phan 3 cau 1

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
    for i in set(dstu):
    print(f" tu {i} xuat hien {dstu.count(i)} lan")

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

    n=str(input("Hãy nhập vào chuỗi: "))
    print("Số lần xuất hiện của từ trong chuỗi là: ", demsolanxuathiencuatu(n))

if __name__=="__main__":
    main()
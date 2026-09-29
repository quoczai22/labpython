class LibraryBook:
    def __init__(self, book_id="", title="", author="", is_borrowed=False):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed

    def display(self):
        tt="Da muon" if self.is_borrowed else "Co san"
        print(f"Ma sach: {self.book_id:<8} | Ten: {self.title:<30} | Tac gia: {self.author:<20} | {tt}")


class LibraryManager:
    def __init__(self):
        self.books=[]

    def add_book(self, book):
        for b in self.books:
            if b.book_id==book.book_id:
                print(f"Ma sach {book.book_id} da ton tai!")
                return False
        self.books.append(book)
        return True

    def borrow_book(self, book_id):
        for b in self.books:
            if b.book_id==book_id:
                if b.is_borrowed:
                    print(f"Muon sach that bai: Cuon sach '{b.title}' ({book_id}) da co nguoi muon!")
                    return False
                b.is_borrowed=True
                print(f"Muon sach thanh cong: '{b.title}' ({book_id})")
                return True
        print(f"Khong tim thay sach co ma {book_id}!")
        return False

    def return_book(self, book_id):
        for b in self.books:
            if b.book_id==book_id:
                if not b.is_borrowed:
                    print(f"Sach '{b.title}' ({book_id}) chua duoc muon, khong the tra!")
                    return False
                b.is_borrowed=False
                print(f"Tra sach thanh cong: '{b.title}' ({book_id})")
                return True
        print(f"Khong tim thay sach co ma {book_id}!")
        return False

    def search_by_title(self, keyword):
        print(f"\n--- KET QUA TIM KIEM THEO TU KHOA: '{keyword}' ---")
        kw=keyword.lower().strip()
        results=[b for b in self.books if kw in b.title.lower()]
        if not results:
            print("Khong tim thay sach phu hop.")
        else:
            for b in results:
                b.display()
        return results

    def display_all(self):
        print("\n--- TOAN BO DAU SACH TRONG THU VIEN ---")
        for b in self.books:
            b.display()


def main():
    lib=LibraryManager()
    lib.add_book(LibraryBook("B01", "Lap trinh Python Co Ban", "Nguyen Van A"))
    lib.add_book(LibraryBook("B02", "Python Nang Cao va OOP", "Tran Thi B"))
    lib.add_book(LibraryBook("B03", "Cau truc du lieu & Giai thuat", "Le Hoang C"))
    lib.add_book(LibraryBook("B04", "Machine Learning voi Python", "Pham Thi D"))

    lib.display_all()

    print("\n--- THUC HIEN MUON SACH ---")
    lib.borrow_book("B01")
    lib.borrow_book("B01") # thu muon lai

    print("\n--- THUC HIEN TRA SACH ---")
    lib.return_book("B01")

    lib.search_by_title("Python")


if __name__=="__main__":
    main()

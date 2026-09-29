class Book:
    book_count=0

    def __init__(self):
        self.book_id=""
        self.title=""
        self.author=""
        Book.book_count+=1

    def input(self):
        self.book_id=input("Hay nhap ma sach: ")
        self.title=input("Hay nhap tieu de sach: ")
        self.author=input("Hay nhap ten tac gia: ")

    def display(self):
        print(f"Ma sach la: {self.book_id} Tieu de sach la: {self.title} Ten tac gia cua sach: {self.author}")

    @classmethod
    def show_count(cls):
        print(f"So luong sach da tao: {cls.book_count}")

def main():
    Book.show_count()
    sach1=Book()
    sach1.input()
    sach1.display()
    Book.show_count()

if __name__=="__main__":
    main()
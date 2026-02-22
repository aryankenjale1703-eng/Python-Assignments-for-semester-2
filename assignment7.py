class library:
    def __init__(self,book,author,available= True):
        self.author = author
        self.book = book
        self.available = available

    def check_out(self):
        if self.available:
            self.available = False
            print(f'"{self.book}"has been checked out. ')
        else:
            print(f'"{self.book}"is currently not available.')

    def return_book(self):
        self.available = True
        print(f'"{self.book}"has been returned and is now available')

    def display_book(self):
        status = "Available" if self.available else "Not available"
        print(f"book name:self{self.book},Author:{self.author},status:{status}")

book1 = library("python programming","guido van Rossum")
book2 = library("Data structure", "mark allen weiss")

book1.display_book()
book1.check_out()
book1.display_book()

book1.return_book()
book1.display_book()
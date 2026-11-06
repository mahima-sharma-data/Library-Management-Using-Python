class Library:
    def __init__(self,totalbook):
        self.totalbook = totalbook
        self.availablebook = totalbook

    def issue_book(self,no_of_book):
        if(no_of_book <=self.availablebook):
            print(f"{no_of_book} books are issued")
            self.availablebook -= no_of_book
        else:
            print(f"{no_of_book} books are not available")
        print(f"only{self.availablebook} books are available")

    def add_book(self,no_of_book):
        self.totalbook +=no_of_book
        self.availablebook +=no_of_book
        print(f"{no_of_book} books are added")
        print(f"Now available books are {self.availablebook}")

    def return_book(self, no_of_book):
        issuebook = self.totalbook - self.availablebook
        if( no_of_book <= issuebook):
            print(f"{no_of_book} books are returned successfully")
            self.availablebook += no_of_book
        else:
            print("you returned extra books")
        print(f"Now {self.availablebook} books are available")

    def show_available_book(self):
        print(f"finally {self.availablebook} books are available")


l1 = Library(100)
l1.issue_book(60)
l1.return_book(30)
l1.add_book(40)
l1.show_available_book()

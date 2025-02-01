class Book:
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("ISBN:",self.isbn)
        
if __name__ == "__main__":
    title = input("Enter the Title: ")
    author = input("Enter the Author: ")
    isbn = input("Enter the ISBN: ")
    book = Book(title, author, isbn)
    book.display()
    
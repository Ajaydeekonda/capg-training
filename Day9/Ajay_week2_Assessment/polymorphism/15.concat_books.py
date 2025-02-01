class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages)"

    
    def __add__(self, other):
        if isinstance(other, Book): 
            new_title = f"{self.title} & {other.title}" 
            new_pages = self.pages + other.pages 
            return Book(new_title, f"{self.author} and {other.author}", new_pages)
        return NotImplemented 



book1 = Book("Python Basics", "Alice", 300)
book2 = Book("Advanced Python", "Bob", 400)


series = book1 + book2


print(series)

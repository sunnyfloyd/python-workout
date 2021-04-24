class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl:
    def __init__(self) -> None:
        self.scoops = []

    def add_scoops(self, *flavors):
        self.scoops.extend(flavors)

    def __repr__(self) -> str:
        return '\n'.join(scoop.flavor for scoop in self.scoops)


class Book:
    def __init__(self, title, author, price, width) -> None:
        self.title = title
        self.author = author
        self.price = price
        self.width = width


class Shelf:
    def __init__(self) -> None:
        self.books = []
        self.remaining_width = 100

    def add_book(self, *books):
        if self.remaining_width - sum(book.width for book in books) < 0:
            raise Exception('Not enough space on the shelf!')
        self.books.extend(books)

    def total_price(self):
        return sum(book.price for book in self.books)
    
    def has_book(self, book_to_find):
        return book_to_find in [book.title for book in self.books]


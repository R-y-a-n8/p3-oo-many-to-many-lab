from lib.many_to_many import Author, Book, Contract

class Author:
    all_authors = []
    
    def __init__(self, name):
        self.name = name
        self._contracts = []
        type(self).all_authors.append(self)
    
    def contracts(self):
        return self._contracts.copy()

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an integer")
        if royalties < 0 or royalties > 100:
            raise ValueError("royalties must be between 0 and 100")
        
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:
    all_books = []
    
    def __init__(self, title):
        self.title = title
        type(self).all_books.append(self)


class Contract:
    all_contracts = []
    
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an integer")
        if royalties < 0 or royalties > 100:
            raise ValueError("royalties must be between 0 and 100")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        type(self).all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]

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
            return None
        if not isinstance(date, str):
            return None
        if not isinstance(royalties, int):
            return None
        if royalties < 0 or royalties > 100:
            return None
        
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
            return
        if not isinstance(book, Book):
            return
        if not isinstance(date, str):
            return
        if not isinstance(royalties, int):
            return
        if royalties < 0 or royalties > 100:
            return
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        type(self).all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]

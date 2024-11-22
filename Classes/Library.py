import json
from Classes.Book import Book


class Library:
    def __init__(self, filename='library.json'):
        self.books = []
        self.filename = filename
        self.load_books()

    def load_books(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for item in data:
                    book = Book(item['title'], item['author'], item['year'])
                    book.id = item['id']
                    book.status = item['status']
                    self.books.append(book)
        except FileNotFoundError:
            self.books = []

    def save_books(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int):
        new_book = Book(title, author, year)
        new_book.id = len(self.books) + 1  # генерируем уникальный id
        self.books.append(new_book)
        self.save_books()

    def remove_book(self, book_id: int):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                return
        print("книга с таким ID не найдена.")

    def search_book(self, query: str):

        results = [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower() or query == str(book.year)]
        return results

    def display_books(self):
        for book in self.books:
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")

    def change_status(self, book_id: int, new_status: str) -> str:
        for book in self.books:
            if book.id == book_id:
                if new_status in ["в наличии", "выдана"]:
                    book.status = new_status
                    self.save_books()
                    print(type(self.save_books()))
                    return
                else:
                    print("вы ввели неверное значение, попробуйте еще раз")
                    return
        print("книга с таким ID не найдена.")


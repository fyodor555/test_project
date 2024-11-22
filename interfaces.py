from main import Library


def validate(text: str) -> int:
    while True:
        try:
            num = int(input(text))
            break
        except ValueError:
            print("это не число")
    return num


def add_book_interface(library: Library):
    title = input("введите title: ")
    author = input("введите author: ")
    year = validate("введите year: ")
    library.add_book(title, author, year)


def remove_book_interface(library: Library):
    book_id = int(input("введите ID книги для удаления: "))
    library.remove_book(book_id)


def search_book_interface(library: Library):
    query = input("введите название, автора или год, чтобы выполнить поиск:")
    results = library.search_book(query)
    if results:
        for book in results:
            print(
                f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")
    else:
        print("книги не найдены.")


def change_status_interface(library: Library):
    book_id = int(input("введите ID книги для изменения статуса: "))
    new_status = input("введите новый статус (в наличии/выдана): ")
    library.change_status(book_id, new_status)

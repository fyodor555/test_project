from interfaces import *
from Classes.Library import Library


def main():
    library = Library()

    actions = {
        '1': lambda: add_book_interface(library),
        '2': lambda: remove_book_interface(library),
        '3': lambda: search_book_interface(library),
        '4': lambda: library.display_books(),
        '5': lambda: change_status_interface(library),
        '6': lambda: exit()
    }

    while True:
        print("\n1. добавить книгу")
        print("2. удалить книгу")
        print("3. найти книги")
        print("4. отобразить все книги")
        print("5. изменить статус книги")
        print("6. выход")

        choice = input("выберите действие: ")

        action = actions.get(choice)
        if action:
            action()
        else:
            print("неверный выбор, попробуйте снова.")


if __name__ == '__main__':
    main()

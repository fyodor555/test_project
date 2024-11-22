class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"
        self.id = None  # будет установлен позже

    def to_dict(self) -> dict:
        book = {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status}
        return book

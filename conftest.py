import pytest

from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
    collector.get_book_genre('Гордость и предубеждение и зомби')
    collector.get_books_with_specific_genre('Ужасы')
    collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
    collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
    return collector
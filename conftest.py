import pytest

from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
    collector.get_book_genre('Гордость и предубеждение и зомби')
    collector.get_books_with_specific_genre('Ужасы')
    collector.add_book_in_favorites('Гордость и предубеждение и зомби')
    collector.get_list_of_favorites_books('Гордость и предубеждение и зомби')
    collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

    return collector
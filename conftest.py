import pytest

from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    collector.add_new_book()
    collector.add_new_book()
    collector.set_book_genre()
    collector.get_book_genre()
    collector.add_book_in_favorites()
    collector.get_books_for_children()
    collector.get_books_with_specific_genre()
    collector.delete_book_from_favorites()
    collector.get_list_of_favorites_books()
    return collector
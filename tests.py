import pytest
from main import BooksCollector
class TestBooksCollector:

    @pytest.mark.parametrize('name_book', ['Что делать, если ваш кот хочет вас убить Что делать, если ваш кот хочет вас убить', 'йййййййййййййййцццццццццццццууууууууууууу', 'qqqqqqqqqqqqqqq ццццццццццццц eeeeeeeeeeee'])
    def test_negative_add_book(self, collector, name_book):
        collector = BooksCollector()
        collector.add_new_book(name_book)
        assert not len(collector.get_books_genre()) == 1


    def test_add_new_book_add_two_books(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2
    # напиши свои тесты ниже
    def test_add_new_book_duble_add_books(self, collector):
        #создаем экземпляр (объект) класса BooksCollector
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert (len(collector.get_books_genre())) == 1

    def test_add_new_book_more_41_add_books(self, collector):
        #создаем экземпляр (объект) класса BooksCollector
        collector.add_new_book('Гордость и предубеждение и зомби Гордость и предубеждение и зомби')
        assert (len(collector.get_books_genre())) == 0
    def test_set_horror_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'
    def test_get_horror_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_books_with_two_books_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']

    def test_get_key_val_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость')
        collector.set_book_genre('Гордость', 'Ужасы')
        collector.add_new_book('Что делать')
        collector.set_book_genre('Что делать', 'Детективы')
        assert collector.get_books_genre() == {'Гордость': 'Ужасы', 'Что делать': 'Детективы'}
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') == 'Комедии'

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.books_genre = {'Что делать, если ваш кот хочет вас убить': 'Комедии' }
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert 'Что делать, если ваш кот хочет вас убить' in collector.get_list_of_favorites_books()

    def test_add_book_double_in_favorites(self):
        collector = BooksCollector()
        collector.books_genre = {'Что делать, если ваш кот хочет вас убить': 'Комедии' }
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert 'Что делать, если ваш кот хочет вас убить' not in collector.get_list_of_favorites_books()
import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_one_book_book_added(self, collector, book_all_ages):
        collector.add_new_book(book_all_ages)
        assert book_all_ages in collector.books_genre and len(collector.books_genre) == 1

    @pytest.mark.parametrize(
        'invalid_book_name',
        ['',
         'Long book name for testing - more then 41 symbol'
         ]
    )
    def test_add_new_book_add_one_book_not_added(self, collector, invalid_book_name):
        collector.add_new_book(invalid_book_name)
        assert invalid_book_name not in collector.books_genre and len(collector.books_genre) == 0

    def test_set_book_genre_set_existing_genre_genre_set(self, collector, book_all_ages, genre_all_ages):
        collector.add_new_book(book_all_ages)
        collector.set_book_genre(book_all_ages, genre_all_ages)
        assert collector.books_genre[book_all_ages] == genre_all_ages

    def test_set_book_genre_set_not_existing_genre_genre_not_set(self, collector, book_all_ages):
        collector.add_new_book(book_all_ages)
        collector.set_book_genre(book_all_ages, 'Триллер')
        assert collector.books_genre[book_all_ages] == ''

    def test_get_book_genre_get_genre_genre_correct(self, collector, book_all_ages, genre_all_ages):
        collector.add_new_book(book_all_ages)
        collector.set_book_genre(book_all_ages, genre_all_ages)
        assert collector.get_book_genre(book_all_ages) == genre_all_ages

    def test_get_books_with_specific_genre_get_book_with_genre_list_correct(self, collector, book_all_ages,
                                                                            genre_all_ages,
                                                                            book_age_rating, genre_age_rating):
        collector.add_new_book(book_all_ages)
        collector.set_book_genre(book_all_ages, genre_all_ages)
        collector.add_new_book(book_age_rating)
        collector.set_book_genre(book_age_rating, genre_age_rating)
        assert len(collector.get_books_with_specific_genre(
            genre_age_rating)) == 1 and book_age_rating in collector.get_books_with_specific_genre(
            genre_age_rating)

    def test_get_books_for_children_get_child_books_list_correct(self, collector, book_all_ages, genre_all_ages,
                                                                 book_age_rating,
                                                                 genre_age_rating):
        collector.add_new_book(book_all_ages)
        collector.set_book_genre(book_all_ages, genre_all_ages)
        collector.add_new_book(book_age_rating)
        collector.set_book_genre(book_age_rating, genre_age_rating)
        assert len(
            collector.get_books_for_children()) == 1 and book_all_ages in collector.get_books_for_children()

    def test_add_book_in_favorites_add_one_book_book_added(self, collector, book_age_rating):
        collector.add_new_book(book_age_rating)
        collector.add_book_in_favorites(book_age_rating)
        assert book_age_rating in collector.favorites and len(collector.favorites) == 1

    def test_add_book_in_favorites_add_same_book_book_not_added(self, collector, book_age_rating):
        collector.add_new_book(book_age_rating)
        collector.add_book_in_favorites(book_age_rating)
        collector.add_book_in_favorites(book_age_rating)
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_remove_one_book_book_removed(self, collector, book_all_ages):
        collector.add_new_book(book_all_ages)
        collector.add_book_in_favorites(book_all_ages)
        collector.delete_book_from_favorites(book_all_ages)
        assert book_all_ages not in collector.favorites and len(collector.favorites) == 0

    def test_get_list_of_favorites_books_get_list_list_returned(self, collector, book_all_ages):
        collector.add_new_book(book_all_ages)
        collector.add_book_in_favorites(book_all_ages)
        assert book_all_ages in collector.get_list_of_favorites_books() and len(
            collector.get_list_of_favorites_books()) == 1

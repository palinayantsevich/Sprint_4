import pytest

from main import BooksCollector


@pytest.fixture(scope='function')
def collector():
    return BooksCollector()


@pytest.fixture(scope='function')
def book_all_ages():
    book_all_ages = 'Приключения Алисы в Стране Чудес'
    return book_all_ages


@pytest.fixture(scope='function')
def genre_all_ages():
    genre_all_ages = 'Мультфильмы'
    return genre_all_ages


@pytest.fixture(scope='function')
def book_age_rating():
    book_age_rating = 'Дракула'
    return book_age_rating


@pytest.fixture(scope='function')
def genre_age_rating():
    genre_age_rating = 'Ужасы'
    return genre_age_rating

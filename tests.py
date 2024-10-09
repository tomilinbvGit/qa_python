from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    def test_add_new_book_book_added(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Три стигмата Палмера Элдрича')

        # проверяем, что книга добавлена
        assert len(collector.books_genre) == 1

    def test_add_new_book_add_two_identical_books_one_is_added(self):  #пробуем добавить две одинаковые книги
        collector = BooksCollector()

        collector.add_new_book('Пролейтесь, слёзы...')
        collector.add_new_book('Пролейтесь, слёзы...')

        assert len(collector.books_genre) == 1  #проверяем, что добавлена только одна книга

    def test_set_book_genre_genre_sets(self):  #тестируем установку жанра для книги
        collector = BooksCollector()

        collector.add_new_book('Мечтают ли андроиды об электроовцах?')
        collector.set_book_genre('Мечтают ли андроиды об электроовцах?', 'Фантастика')

        assert collector.books_genre[
                   'Мечтают ли андроиды об электроовцах?'] == 'Фантастика'  #проверяем, что жанр установлен

    def test_set_book_genre_set_genre_not_from_list(self):  #тестируем установку жанра не из списка
        collector = BooksCollector()

        collector.add_new_book('Сдвиг времени по-марсиански')
        collector.set_book_genre('Сдвиг времени по-марсиански', 'Хроноопера')

        assert collector.books_genre['Сдвиг времени по-марсиански'] is ''  #жанр не будет добавлен

    def test_get_book_genre_genre_returned(self):
        collector = BooksCollector()

        collector.add_new_book('Свидание с Рамой')
        collector.set_book_genre('Свидание с Рамой', 'Фантастика')

        assert collector.get_book_genre('Свидание с Рамой') == 'Фантастика'

    def test_get_books_with_specific_genre_the_correct_list_is_displayed(self):  #проверяем, что выводятся книги только с указанным жанром
        collector = BooksCollector()

        collector.add_new_book('Франкенштейн, или Современный Прометей')
        collector.set_book_genre('Франкенштейн, или Современный Прометей', 'Ужасы')

        collector.add_new_book('Тень над Иннсмутом')
        collector.set_book_genre('Тень над Иннсмутом', 'Ужасы')

        collector.add_new_book('Дети Мафусаила')
        collector.set_book_genre('Дети Мафусаила', 'Фантастика')

        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2

    def test_get_books_genre_all_elements_are_displayed(self):
        collector = BooksCollector()

        collector.add_new_book('Лунный камень')
        collector.add_new_book('Ошибка резидента')
        collector.add_new_book('Незнайка на Луне')

        assert len(collector.get_books_genre()) == 3

    def test_get_books_for_children_returned_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Мечтают ли андроиды об электроовцах?')
        collector.set_book_genre('Мечтают ли андроиды об электроовцах?', 'Фантастика')

        collector.add_new_book('Тень над Иннсмутом')
        collector.set_book_genre('Тень над Иннсмутом', 'Ужасы')

        collector.add_new_book('Незнайка на Луне')
        collector.set_book_genre('Незнайка на Луне', 'Комедии')

        collector.add_new_book('Маленький принц')
        collector.set_book_genre('Маленький принц', 'Мультфильмы')

        needed_books = ['Мечтают ли андроиды об электроовцах?', 'Незнайка на Луне', 'Маленький принц']

        assert all(book in collector.get_books_for_children() for book in needed_books)

    @pytest.mark.parametrize('name', ['Дюна', '451 градус по Фаренгейту', 'Задача трёх тел'])
    def test_add_book_in_favorites_book_added(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)

        assert name in collector.favorites

    @pytest.mark.parametrize('name', ['Дюна', '451 градус по Фаренгейту', 'Задача трёх тел'])
    def test_delete_book_from_favorites_book_deleted(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)

        assert name not in collector.favorites

    def test_get_list_of_favorites_books_list_returned(self):
        collector = BooksCollector()

        collector.add_new_book('Мечтают ли андроиды об электроовцах?')
        collector.add_book_in_favorites('Мечтают ли андроиды об электроовцах?')

        collector.add_new_book('Тень над Иннсмутом')
        collector.add_book_in_favorites('Тень над Иннсмутом')

        collector.add_new_book('Незнайка на Луне')
        collector.add_book_in_favorites('Незнайка на Луне')

        needed_books = ['Мечтают ли андроиды об электроовцах?', 'Тень над Иннсмутом', 'Незнайка на Луне']

        assert all(book in collector.get_list_of_favorites_books() for book in needed_books)

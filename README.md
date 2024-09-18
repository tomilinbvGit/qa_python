# qa_python

ТЕСТ test_add_new_book_add_two_books - проверка метода add_new_book:
    Добавлям книгу через метод add_new_book.
    Результат проверяем через длину books_genre.

ТЕСТ test_add_new_book_add_two_identical_books_one_is_added - проверка метода add_new_book (отрицательная проверка):
    Добавляем две одинаковые книги.
    Результат проверяем через проверку длины books_genre.

ТЕСТ test_set_book_genre_genre_sets - проверка метода set_book_genre (положительная проверка):
    Добавляем книгу и добавляем ей жанр
    Результат проверяем через обращение к словарю по ключу (название книги).

ТЕСТ test_set_book_genre_set_genre_not_from_list - проверка метода set_book_genre (отрицательная проверка):
    Добавляем книгу и добавляем ей жанр не из списка.
    Результат проверяем через обращение к словарю books_genre по ключу (название книги).

ТЕСТ test_get_book_genre_genre_returned - проверка метода get_book_genre:
    Добавляем книгу и добавляем ей жанр из списка.
    Результат проверяем через обращение к словарю books_genre по ключу (название книги).

ТЕСТ test_get_books_with_specific_genre_the_correct_list_is_displayed - проверка метода get_books_with_specific_genre:
    Добавляем книги разных жанров и добавляем им жанры.
    Результат проверяем через длину списка books_with_specific_genre.

ТЕСТ test_get_books_genre_all_elements_are_displayed - проверка метода get_books_genre:
    Добавляем книги в через метод add_new_book.
    Результат проверяем через длину books_genre.

ТЕСТ test_get_books_for_children_returned_books_for_children - проверка метода get_books_for_children:
    Добавляем книги и жанры к ним.
    Результат метода проверяем через длину списка books_for_children.

ТЕСТ test_add_book_in_favorites_book_added - проверка метода add_book_in_favorites:
    Добавляем книгу в books_genre и добавляем книгу в список favorites.
    Результат проверяем через вхождение книги в список favorites.

ТЕСТ test_delete_book_from_favorites_book_deleted - проверка метода delete_book_from_favorites:
    Добавляем книгу в books_genre, добавляем книгу в список favorites и удаляем книгу из списка favorites.
    Результат проверяем через вхождение книги в список favorites.
    
ТЕСТ test_get_list_of_favorites_books_list_returned - проверка метода get_list_of_favorites_books:
    Добавляем книги в books_genre и добавляем их в список favorites.
    Результат проверяем через проверку длину списка favorites.
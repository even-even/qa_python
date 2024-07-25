import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_adding_three_books_success(self, collection):
        """Проверка добавления трех книг в словарь books_genre"""

        books = ('Ромео и Джульетта', 'Мастер и Маргарита', 'Король Лев')
        for book in books:
            collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 3

    def test_add_new_book_check_genre_success(self, collection):
        """Проверка установления жанра по умолчанию в добавленной книге"""

        first_book = 'Ромео и Джульетта'
        collection.add_new_book(first_book)
        assert collection.get_book_genre(first_book) == ''

    @pytest.mark.parametrize('book',
                             ['', 'МастерМастерМастерМастерМастерМастерМастер']
                             )
    def test_add_new_book_add_incorrect_name_not_added(self, book, collection):
        """Негативная проверка добавления книг с именем 0 и больше 40 символов"""

        collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 0

    def test_add_new_book_add_double_books_not_added(self, collection):
        """Негативная проверка повторного добавления одинаковых книг"""

        books = ['Война и мир', 'Война и мир']
        for book in books:
            collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 1

    def test_set_book_genre_added(self, collection):
        """Проверка добавления жанра из списка genre книге из списка books_genre"""

        first_book = 'Властелин колец'
        genre = 'Фантастика'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book, genre)
        assert collection.get_book_genre(first_book) == genre

    def test_set_book_genre_changed(self, collection):
        """Проверка изменения жанра из списка genre книге из списка books_genre"""

        first_book = 'Властелин колец'
        genre = 'Фантастика'
        other_genre = 'Детективы'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book, genre)
        collection.set_book_genre(first_book, other_genre)
        assert collection.get_book_genre(first_book) == other_genre

    def test_set_book_genre_missing_genre_not_added(self, collection):
        """Негативная проверка добавления жанра не из списка genre книге из списка books_genre"""

        first_book = 'Властелин колец'
        missing_genre = 'Приключения'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book, missing_genre)
        assert collection.get_book_genre(first_book) == ''

    def test_get_books_with_specific_genre_success(self, collection_five_books):
        """Проверка вывода книги определенного жанра"""

        assert collection_five_books.get_books_with_specific_genre('Ужасы') == ['Чужой']

    def test_get_books_with_specific_genre_missing_book(self, collection_five_books):
        """Негативная проверка вывода отсутствующей книги определенного жанра"""

        assert len(collection_five_books.get_books_with_specific_genre('Приключения')) == 0

    def test_get_books_for_children_success(self, collection_five_books):
        """Проверка вывода списка книг с жанром для детей"""

        children_books = collection_five_books.get_books_for_children()
        assert len(children_books) == 3 and children_books == ['Властелин колец', 'Король лев', 'Сон в летнюю ночь']

    def test_add_book_in_favorites_add_one_book_added(self, collection):
        """Проверка добавления книги из списка books_genre в избранное"""

        first_book = 'Хоббит'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        favorites = collection.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == first_book

    def test_add_book_in_favorites_add_missing_book_not_added(self, collection):

        first_book = 'Властелин колец'
        collection.add_book_in_favorites(first_book)
        assert len(collection.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_add_double_books_not_added(self, collection):
        """Негативная проверка повторного добавления книги в избранное"""

        first_book = 'Властелин колец'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        collection.add_book_in_favorites(first_book)
        favorites = collection.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == first_book

    def test_delete_book_from_favorites_book_deleted(self, collection):
        """Проверка удаления книги из списка избранное"""

        first_book = 'Властелин колец'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        collection.delete_book_from_favorites(first_book)
        assert len(collection.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_missing_book_not_deleted(self, collection):
        """Негативная проверка удаления не добавленной книги в favorites"""

        first_book = 'Хоббит'
        second_book = 'Властелин колец'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        collection.delete_book_from_favorites(second_book)
        favorites = collection.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == first_book

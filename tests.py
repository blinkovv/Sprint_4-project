from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book(self):  # Добавление новой книги
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        assert "Война и мир" in collector.books_genre
        assert collector.books_genre["Война и мир"] == ""

    def test_set_book_genre(self):  # Установка жанра для книги
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Классика")
        assert collector.books_genre["Война и мир"] == "Классика"

    def test_get_book_genre(self):  # Получение жанра книги
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Классика")
        assert collector.get_book_genre("Война и мир") == "Классика"

    def test_get_books_with_specific_genre(self):  # Получение книги с определенным жанром
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Классика")
        collector.add_new_book("Преступление и наказание")
        collector.set_book_genre("Преступление и наказание", "Классика")
        assert collector.get_books_with_specific_genre("Классика") == ["Война и мир", "Преступление и наказание"]

    def test_get_books_genre(self):  # Получение словаря книг с жанрами
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Классика")
        collector.add_new_book("Преступление и наказание")
        collector.set_book_genre("Преступление и наказание", "Классика")
        assert collector.get_books_genre() == {"Война и мир": "Классика", "Преступление и наказание": "Классика"}

    def test_get_books_for_children(self):  # Список книг для детей
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Классика")
        collector.add_new_book("Маленький принц")
        collector.set_book_genre("Маленький принц", "Сказка")
        collector.add_new_book("Кошмар на улице Вязов")
        collector.set_book_genre("Кошмар на улице Вязов", "Ужасы")
        assert collector.get_books_for_children() == ["Маленький принц"]

    def test_add_book_in_favorites(self):  # Добавление книги в избранное
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        assert "Война и мир" in collector.favorites

    def test_delete_book_from_favorites(self):  # Удаление книги из избранного
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        collector.delete_book_from_favorites("Война и мир")
        assert "Война и мир" not in collector.favorites

    def test_get_list_of_favorites_books(self):  # Получение списка избранных книг
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_new_book("Преступление и наказание")
        collector.add_book_in_favorites("Война и мир")
        collector.add_book_in_favorites("Преступление и наказание")
        assert collector.get_list_of_favorites_books() == ["Война и мир", "Преступление и наказание"]

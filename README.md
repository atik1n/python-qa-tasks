# Задание 1 - pytest - WikiPyTest
- На сайте https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites есть таблица «Programming languages used in most popular websites».
- Необходимо реализовать параметризованный тест, проверяющий, что в этой таблице нет строк, у которых значение в столбце «Popularity (unique visitors per month)» меньше передаваемого в качестве параметра в тест значения.
- Если такие строки в таблице есть, тест выводит сообщение об ошибке, перечисляя строки с ошибками в виде, пример: “Wikipedia (Frontend:JavaScript|Backend:PHP) has 475 000 000 unique visitors per month. (Expected more than 500 000 000)”.
- Тест должен запускаться для значений: [10^7, 1.5 * 10^7, 5 * 10^7, 10^8, 5 * 10^8, 10^9, 1.5 * 10^9]
- При реализации теста необходимо учитывать, что данные из этой таблицы могут понадобиться и в других тестах. Будет плюсом реализовать хранение данных из таблицы в виде датаклассов.

# Задание 2 - ООП - Graphics
- Реализовать 2D-движок, который умеет “рисовать” простейшие двумерные примитивы на экране. Сам движок должен быть представлен в виде объекта класса Engine2D.
- Движок должен иметь “холст” (canvas) и возможность добавлять на него фигуры. Холст будет содержать текущий список примитивов для отрисовки.
- Реализовать классы для 3-х геометрических фигур: окружность, треугольник, прямоугольник. Необходимые параметры для создания фигур выбрать самостоятельно.
- Каждая фигура должна иметь метод draw(), при вызове которого выводится информация в виде print’а, например “Drawing Circle: (0, 1) with radius 5”.
- При завершении добавления фигур, у движка необходимо вызвать публичный метод draw(), который последовательно вызовет методы для отрисовки у всех фигур на холсте и очистит его.
- Добавить возможность менять цвет отрисовки, путем вызова публичного метода у движка (можно воспринимать это как «смена карандаша»):
    - После вызова этого метода, все последующие фигуры должны рисоваться указанным цветом, до очередного выставления нового цвета.
    - В тексте “отрисовки” фигуры должен появиться цвет, которым она будет рисоваться.
- Написать юниттесты с использованием pytest. Необходимое количество тестов определить самостоятельно.
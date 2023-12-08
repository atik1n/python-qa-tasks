# Задание 1 - pytest

## wiki_table.py
Здесь находится код, что получает нужную нам таблицу при помощи API Википедии и преобразует её в "переваримый" вид, заодно убирая лишние WikiText и HTML тэги.

## wiki_table_test.py
Здесь описаны тесты, а именно проверка, что в столбце «Popularity (unique visitors per month)» все значения больше заданного, а если нет - то выводится строка в виде `“Wikipedia (Frontend:JavaScript|Backend:PHP) has 475 000 000 unique visitors per month. (Expected more than 500 000 000)”`
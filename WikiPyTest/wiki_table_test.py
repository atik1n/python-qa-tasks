import pytest
import wiki_table

from wiki_table import Website

test_values = [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9]


def failed_string(min_value: int, sites: list[Website]) -> str:
    """
    Метод, генерирующий строку для вывода вместе с провалом теста.

    :param int min_value: Минимально необходимое количество посетителей
    :param list[Website] sites: Вебсайты у которых значение ниже порогового значения
    :return: Строка с информацией
    :rtype: str
    """
    substrings = [''] + [(f"{site.name} (Frontend:{site.frontend}|Backend:{site.backend}) has {site.popularity} "
                          f"unique visitors per month. (Expected more than {min_value})") for site in sites]

    return '\n'.join(substrings)


@pytest.mark.parametrize("min_value", test_values)
def test_table(min_value: int):
    """
    Тест, проверяющий, что все сайты в таблице имеют количество посетителей больше порогового значения.

    :param int min_value: Минимально необходимое количество посетителей
    """
    failed: list[Website] = list()

    table = wiki_table.get_wiki_table()
    for row in table:
        if row.popularity < min_value:
            failed += [row]

    ff = not failed  # Флаг, чтобы вывод не содержал в себе list[Website]
    assert ff, f"{failed_string(min_value, failed)}"

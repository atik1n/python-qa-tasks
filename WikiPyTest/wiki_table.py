import json
import requests
import string
import wikitextparser

from dataclasses import dataclass


wiki_page_name = "Programming_languages_used_in_most_popular_websites"
wiki_table_caption = "Programming languages used in most popular websites"
wiki_api_url = string.Template("https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles=$page&formatversion=2&rvprop=content&rvslots=*")


@dataclass
class Website:
    """Dataclass для строки в таблице."""
    name: str
    popularity: int
    frontend: str
    backend: str
    database: str
    notes: str

    def __post_init__(self):
        """Преобразует popularity к int, убирая разделители и примечания."""
        if isinstance(self.popularity, str):
            self.popularity = self.popularity.replace(',', '')  # Есть запятые
            self.popularity = self.popularity.replace('.', '')  # А ещё есть точки
            self.popularity = self.popularity.split(' ')[0]  # А ещё есть примечания
            self.popularity = int(self.popularity)


def get_wiki_table() -> list[Website]:
    """
    Метод, возвращающий таблицу Programming languages used in most popular websites
    со страницы в Википедии Programming languages used in most popular websites

    :rtype: list[Website]
    """

    r = requests.get(wiki_api_url.substitute(page=wiki_page_name))
    jr = json.loads(r.content)

    page = jr["query"]["pages"][0]
    if "missing" not in page:
        content = page["revisions"][0]["slots"]["main"]["content"]  # Очень много вложенности в API Википедии
        wt_content = wikitextparser.parse(content)
        if any(table := t for t in wt_content.tables if wiki_table_caption in t.caption):
            parsed_table: list[Website] = list()
            for row in table.data()[1:]:
                parsed_row: list[str] = list()
                for cell in row:
                    cell = cell.replace(" <br />", "").replace("<br />", " ")
                    parsed_cell = wikitextparser.parse(cell)
                    for tag in parsed_cell.get_tags():
                        del tag[:]  # Удаляем лишние тэги, например сноски
                    parsed_row.append(parsed_cell.plain_text())
                parsed_table.append(Website(*parsed_row))
            if parsed_table:
                return parsed_table
    return list()


if __name__ == "__main__":
    print(get_wiki_table())

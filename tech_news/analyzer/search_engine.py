from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    response_db = search_news({'title': {'$regex': title, '$options': 'i'}})
    list_tupas = []
    for tup in response_db:
        list_tupas.append((tup['title'], tup['url']))
    return list_tupas


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


print(search_by_title('UX'))
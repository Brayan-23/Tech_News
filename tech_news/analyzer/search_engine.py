from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    response_db = search_news({'title': {'$regex': title, '$options': 'i'}})
    list_tupas = []
    for tup in response_db:
        list_tupas.append((tup['title'], tup['url']))
    return list_tupas


# Requisito 8
def search_by_date(date):
    try:
        data = datetime.strptime(date, '%Y-%m-%d').date()
        formated = data.strftime('%d/%m/%Y')
        response_db = search_news({'timestamp': {'$regex': formated}})
        list_tuplas = []
        for tup in response_db:
            list_tuplas.append((tup['title'], tup['url']))
        return list_tuplas
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""

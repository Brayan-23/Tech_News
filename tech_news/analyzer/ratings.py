from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_categories():
    categories = find_news()
    lista = []
    for category in categories:
        lista.append(category["category"])

    top_5 = Counter(sorted(lista)).most_common()[:5]

    lista_top_5 = []
    for new_top in top_5:
        lista_top_5.append(new_top[0])

    return lista_top_5

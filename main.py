import requests
from datetime import date, timedelta
from pprint import pprint


# Нужны все вопросы за последние два дня с тэгом "Python"


def get_question():
    url = "https://api.stackexchange.com/2.3/questions"
    from_date = date.today() - timedelta(days=2)
    to_date = date.today()
    params = {
        "page": "1",
        "pagesize": "100",
        "fromdate": from_date,
        "todate": to_date,
        "order": "desc",
        "sort": "creation",
        "tagged": 'Python',
        "filter": "default",
        "site": 'stackoverflow'
    }
    response = requests.get(url, params=params)
    pprint(response.json())


if __name__ == '__main__':
    get_question()

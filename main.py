import requests
import datetime
from pprint import pprint
# Нужны все вопросы за последние два дня с тэгом "Python"

def get_question():
    url = "https://api.stackexchange.com/docs/questions"
    from_date = "2021-12-26"
    to_date = "2021-12-28"
    params = {
        "fromdate": from_date,
        "todate": to_date,
        "tagged": 'Python',
        "order": "desc",
        "filter": "default",
        "site": 'stackoverflow'
    }
    response = requests.get(url, params=params)
    pprint(response.json())


if __name__ == '__main__':
    get_question()

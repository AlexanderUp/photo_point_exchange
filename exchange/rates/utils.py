import requests

from rates.exceptions import UnknownCurrencyError

API_URL: str = 'https://www.cbr-xml-daily.ru/daily_json.js'


def get_rate_json(currency='USD'):
    response = requests.get(API_URL, timeout=10)
    response_json = response.json()
    exchange_date = response_json['Timestamp']

    try:
        exchange_rate = response_json['Valute'][currency]['Value']
    except KeyError as err:
        raise UnknownCurrencyError() from err

    return {
        'timestamp': exchange_date,
        'rate': exchange_rate,
    }

import requests

API_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


class UnknownCurrencyError(Exception):
    pass


def get_rates_json(currency='USD'):
    response = requests.get(API_URL)
    response_json = response.json()
    exchange_date = response_json['Timestamp']

    try:
        exchange_rate = response_json['Valute'][currency]['Value']
    except KeyError as err:
        raise UnknownCurrencyError() from err

    return (exchange_date, exchange_rate)


if __name__ == '__main__':
    print('*' * 125)

    usd_exchange_value = get_rates_json()

    print(usd_exchange_value)
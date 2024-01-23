import datetime

from django.conf import settings
from django.utils import timezone

from rates.models import CurrencyRate
from rates.utils import get_rate_json


def get_current_rate(last_request_time):
    result_dict = {}
    time_since_last_request = timezone.now() - last_request_time

    time_delta = datetime.timedelta(
        seconds=settings.OUTER_API_REQUEST_MIN_PERIOD_SECONDS,
    )

    if time_since_last_request > time_delta:
        actual_time_and_rate: dict = get_rate_json()
        CurrencyRate.objects.create(**actual_time_and_rate)
        result_dict.update({'current': actual_time_and_rate})
    return result_dict


def get_last_rates(results_number=settings.NUMBER_OF_RESULTS_TO_RETURN):
    result_list = []
    ten_lasts = CurrencyRate.objects.values(
        'timestamp',
        'rate',
        'created_at',
    )[:results_number]

    try:
        last_request_time = ten_lasts[0]['created_at']
    except IndexError:
        last_request_time = datetime.datetime(
            1970,
            1,
            1,
            tzinfo=datetime.timezone(datetime.timedelta(0)),
        )

    current_rate = get_current_rate(last_request_time)
    if current_rate:
        result_list.append(current_rate)
    else:
        result_list.append({'current': 'Request to external API throttled.'})

    ten_lasts_formatted = [
        {'timestamp': rate['timestamp'].isoformat(), 'rate': float(rate['rate'])}
        for rate in ten_lasts
    ]
    result_list.append({'ten_last': ten_lasts_formatted})
    return result_list

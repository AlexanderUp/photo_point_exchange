class UnknownCurrencyError(Exception):
    def __str__(self):
        return 'Unknown currency tiker provided.'

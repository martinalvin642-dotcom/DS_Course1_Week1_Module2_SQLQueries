def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency == to_currency:
        return amount
    else:
        return amount * exchange_rates[from_currency][to_currency]



def get_exchange_rate(from_currency, to_currency, exchange_rates):
    return exchange_rates[from_currency][to_currency]
from currency_converter import convert_currency, get_exchange_rate, exchange

amount = 100
from_currency = 'USD'
to_currency = 'EUR'

converted_amount = convert_currency(amount, from_currency, to_currency, exchange)
exchange_rate = get_exchange_rate(from_currency, to_currency, exchange)

print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
print(f"The exchange rate from {from_currency} to {to_currency} is {exchange_rate}")
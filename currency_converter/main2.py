# main.py

from currency_converter import convert_currency, get_exchange_rate,exchange_rates
import currency_converter


amount = 1000
from_currency = 'USD'
to_currency = 'EUR'


converted_amount = currency_converter.convert_currency(amount, from_currency, to_currency, exchange_rates)
currency_converter.exchange_rate = currency_converter.get_exchange_rate(from_currency, to_currency, exchange_rates)

print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
print(f"The exchange rate from {from_currency} to {to_currency} is {currency_converter.exchange_rate}")
# exchange_rates.py

exchange_rates = {
    'USD': {'EUR': 0.85, 'GBP': 0.72, 'JPY': 110.12},
    'EUR': {'USD': 1.18, 'GBP': 0.85, 'JPY': 129.55},
    'GBP': {'USD': 1.39, 'EUR': 1.17, 'JPY': 152.45},
    'JPY': {'USD': 0.0091, 'EUR': 0.0077, 'GBP': 0.0066}
}

def update_exchange_rates(new_rates):
    global exchange_rates
    exchange_rates.update(new_rates)
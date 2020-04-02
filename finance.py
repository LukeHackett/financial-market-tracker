#! /usr/bin/env python3

import yfinance 
from datetime import date, datetime, timedelta

# Hack to get around ssl invalid cert
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def ticker(symbol):
    return yfinance.Ticker(symbol)

def double(value):
    if value is None:
        return None

    return round(float(value), 2)

def currency(value, symbol=''):
    if value is None:
        return None

    return symbol + double(value)

def start_date(value):
    return value - timedelta(days=7)

def end_date(value):
    return value + timedelta(days=1)

def fetch_stock(symbol):
    info = ticker(symbol).info

    return {
        'name': info.get('shortName'),
        'symbol': info.get('symbol'),
        'sector': info.get('sector'),
        'industry': info.get('industry'),
        'exchange': info.get('exchange'),
        'currency': info.get('currency'),
        'history': {
            'date': None,
            'open': None,
            'high': None,
            'low': None,
            'close': None,
            'change': {
                'points': None,
                'percentage': None
            },
            'previous': {
                'date': None,
                'open': None,
                'high': None,
                'low': None,
                'close': info.get('previousClose'),
                'change': {
                    'points': None,
                    'percentage': None
                }
            }
        }
    }

def fetch_history(date, stock):
    # Obtain the history of the symbol (last 7 days)
    history = ticker(stock.get('symbol')).history(interval='1d', start=start_date(date), end=end_date(date))

    # Obtain the last three day's index for calculating the stock history
    date0_index = len(history.index.date) - 1
    date1_index = len(history.index.date) - 2
    date2_index = len(history.index.date) - 3

    # Calculate the history for the given date
    if date0_index > 0 and date1_index > 0:
        date0_summary = history.iloc[date0_index]
        date1_summary = history.iloc[date1_index]

        stock['history']['date'] = date0_summary.name.strftime('%Y-%m-%d')
        stock['history']['open'] = double(date0_summary.get('Open'))
        stock['history']['high'] = double(date0_summary.get('High'))
        stock['history']['low'] = double(date0_summary.get('Low'))
        stock['history']['close'] = double(date0_summary.get('Close'))
        stock['history']['change']['points'] = double(stock['history']['close'] - date1_summary.get('Close'))
        stock['history']['change']['percentage'] = double(stock['history']['change']['points'] / date1_summary.get('Close'))

    # Calculate the history for the given date - 1
    if date1_index > 0 and date2_index > 0:
        date1_summary = history.iloc[date1_index]
        date2_summary = history.iloc[date2_index]

        stock['history']['previous']['date'] = date1_summary.name.strftime('%Y-%m-%d')
        stock['history']['previous']['open'] = double(date1_summary.get('Open'))
        stock['history']['previous']['high'] = double(date1_summary.get('High'))
        stock['history']['previous']['low'] = double(date1_summary.get('Low'))
        stock['history']['previous']['close'] = double(date1_summary.get('Close'))
        stock['history']['previous']['change']['points'] = double(stock['history']['previous']['close'] - date2_summary.get('Close'))
        stock['history']['previous']['change']['percentage'] = double(stock['history']['previous']['change']['points'] / date2_summary.get('Close'))

    return stock

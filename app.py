#! /usr/bin/env python3

import finance
from datetime import date
from pprint import PrettyPrinter

def pprint(value):
    pp = PrettyPrinter(indent=4)
    pp.pprint(value)

if __name__ == '__main__':
    query_date = date(2020, 3, 30)

    # print('***** IAG *****')
    iag = finance.fetch_stock('IAG.L')
    iag = finance.fetch_history(query_date, iag)
    pprint(iag)

    # print('***** FTSE *****')
    ftse = finance.fetch_stock('^FTSE')
    ftse = finance.fetch_history(query_date, ftse)
    pprint(ftse)

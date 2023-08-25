from forex_python.converter import CurrencyRates

c = CurrencyRates()
Currency = c.get_rates('usd')  #convert USD to EURO
print(Currency["JPY"])
# from functools import partial
# from datetime import datetime
# from forex_python.converter import CurrencyRates
# date_obj = datetime(2014, 5, 23, 18, 36, 28, 151012)
             
# c = CurrencyRates()
# CurrencyA = str(input("Введите первую валюту: "))
# CurrencyB = str(input("Введите вторую валюту: "))
# value = input("Введите число: ")
# # Currency = c.get_rate('USD', 'INR', date_obj)
# print("Доступные валюты для обмена: 'USD','IDR', 'BGN' 'ILS', 'GBP', 'DKK', 'CAD', 'JPY',\
#                                     'HUF' 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AUD', 'CHF', \
#                                     'KRW', 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'EUR', 'NOK',\
#                                     'RUB', 'INR', 'MXN', 'CZK', 'BRL', 'PLN', 'PHP', 'ZAR'")
# # print(round(Currency, 3))
# Convert = partial(c.convert(f"{CurrencyA}, {CurrencyB}, {value}"))
# print(Convert)






















import requests
from bs4 import BeautifulSoup as bs
import re
from dateutil.parser import parse

def convert_currency_xe(src, dst, amount):
    def get_digits(text):
        """Returns the digits and dots only from an input `text` as a float
        Args:
            text (str): Target text to parse
        """
        new_text = ""
        for c in text:
            if c.isdigit() or c == ".":
                new_text += c
        return float(new_text)
    
    url = f"https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={src}&To={dst}"
    content = requests.get(url).content
    soup = bs(content, "html.parser")
    exchange_rate_html = soup.find_all("p")[2]
    # get the last updated datetime
    last_updated_datetime = parse(re.search(r"Last updated (.+)", exchange_rate_html.parent.parent.find_all("div")[-2].text).group()[12:])
    return last_updated_datetime, get_digits(exchange_rate_html.text)

if __name__ == "__main__":
    import sys
    source_currency = input("Введите исходяющую валюту: ")
    destination_currency = input("Введите выходяющую валюту: ")
    amount = float(input("Введите сумму: "))
    last_updated_datetime, exchange_rate = convert_currency_xe(source_currency, destination_currency, amount)
    print("Last updated datetime:", last_updated_datetime)
    print(f"{amount} {source_currency} = {exchange_rate} {destination_currency}")
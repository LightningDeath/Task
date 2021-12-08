from requests import get, utils
# from decimal import Decimal

resp = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))


def rates(id_number):
    result = resp.split('ID_valuate:')
    for n in result:
        if id_number.upper() in n:
            print(id_number.upper(), end=' ')
            return float(n.replace('/', '').split('<Value>')[-2].replace(',', '.'))
          # return Decimal(n.replace('/', '').split('Value')[-2].replace(',', '.'))


print(rates("EUR"))
print(rates('USD'))
import re

def parsel_email(e_adress):
    r_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not r_email.match(e_adress):
        raise ValueError(f'wrong email: {e_adress}')
    print(r_email.match(e_adress).groupdict())


for n in ('someone@geekbrains.ru','someone@geekbrainsru','so$meone@geekbrainsru'):
    try:
        parsel_email(n)
    except ValueError as err:
        print(err)
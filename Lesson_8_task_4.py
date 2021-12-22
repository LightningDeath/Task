from functools import wraps


def val_cheker(l_function):
    def _val_cheker(function):

        @wraps(function)
        def wrapp(number):
            if l_function(number):
                print(function(number))
            else:
                raise ValueError(f'wrong val {number}')

        return wrapp

    return _val_cheker


@val_cheker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    a = calc_cube(13)
    print(help(calc_cube))
except (ValueError, TypeError) as err:
    print(err)

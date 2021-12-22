from functools import wraps


def t_logger(function):
    @wraps(function)
    def wrapp(*args, **kwargs):
        number_of_list = [elem for elem in (*args, *kwargs.values())]
        i = [f'{function.__name__}({elem}: {type(elem)})' for elem in number_of_list]
        print(*i, *function(*args, **kwargs), sep=',\n')

    return wrapp


@t_logger
def cube_calc(*x, **y):
    number_of_list = [elem for elem in (*x, *y.values()) if isinstance(elem, int) or isinstance(elem, float)]
    return [n ** 3 for n in number_of_list]


cube_calc(3, 14, 4.5, 45, ui=87, io=5)

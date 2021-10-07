class DecoratorClass:

    def __init__(self, url):
        print('Первый вызов DecoratorClass и передача параметра')
        self.url = url
        self.func = None

    def __call__(self, *args, **kwargs):
        if self.func is None:
            print('Второй вызов DecoratorClass и передача аргументов в функцию')
            self.func = args[0]
            return self
        else:
            print('Вызов функции внутри DecoratorClass и передача аргументов в функцию')
            return self.func(*args, **kwargs)

def decorator(url):
    print('Первый вызов и передача параметра в декоратор', url)

    def wrapper_1(func):
        print('Вызов декоратора')

        def wrapper_2(*args, **kwargs):
            print('Вызов функции внутри декоратора')
            res = func(*args, **kwargs)
            print('result')
            return res

        return wrapper_2

    return wrapper_1

@DecoratorClass(url='class_url')
def some_func(arg):
    for i in range(3):
        print(i, 'some func', arg)

some_func('dfasads')
def upper_decorator(fn):
    def inner(name):
        return fn(name.title())

    return inner


def upper(fn, value):
    return fn(value.title())


@upper_decorator
def hello(name):
    return f"Hello {name.title()}"


@upper_decorator
def goodbye(name):
    return f"Goodbye {name.title()}"


# print(upper(hello, "Andrzej"))
# print(upper(goodbye, "Andrzej"))

# h = upper_decorator(hello)
# print(h('andrzej'))
#
# g = upper_decorator(goodbye)
# print(g('andrzej'))

# print(upper_decorator(hello)('andrzej'))
# print(upper_decorator(goodbye)('andrzej'))

print(hello('andrzej'))

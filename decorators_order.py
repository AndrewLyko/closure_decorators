def upper(fn):
    def inner(name):
        return fn(name).title()

    return inner


def reverse(fn):
    def inner(name):
        return fn(name)[::-1]

    return inner


@upper
@reverse
def hello(name):
    return f"Hello {name}"


print(hello('pawel'))
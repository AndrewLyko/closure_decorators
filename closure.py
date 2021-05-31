def sentence(name):
    age = 36
    lol = 30

    def full_sentence(city):
        return f"I am {name}, {age} years-old, from {city}."

    return full_sentence


# s = sentence("Andrzej")
# print(s("Wroclaw"))
# print(s("Krakow"))

# uuid - universal unique identifier
def gen_uuid():
    idx = 0

    def inner():
        nonlocal idx
        result = idx
        idx += 1
        return result

    return inner


uuid = gen_uuid()


# for _ in range(10):
#    print(uuid())
def my_power(exponent):
    def inner(digit):
        return digit ** exponent

    return inner


power_3 = my_power(3)
power_4 = my_power(4)
power_7 = my_power(7)


def my_power(digit):
    return digit ** 2


print(my_power(5))

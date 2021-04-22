""" Hello. """


def say_hello_to(name):
    print(
        f"Hello {name}! Fantastic morning!  ")


def factorial(num):
    for x in range(1, num):
        res = x * (x + 1)
    return res


if __name__ == "__main__":
    say_hello_to("Leo")

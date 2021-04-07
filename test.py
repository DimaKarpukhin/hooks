def say_hello(name):
    print(f'Hello {name} =)')


def factorial(num):
    for x in range(1, num):
        res = x * (x+1)
    return res


if __name__ == "__main__":
    say_hello()

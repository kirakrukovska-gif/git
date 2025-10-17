def number(max):
    for i in range(max + 1):
        yield 3 ** i
for _ in number(10):
    print(_)
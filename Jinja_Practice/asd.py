def asdf():
    b = 0

    while True:
        a = yield b
        b += a


a = asdf()
a.__next__()
r = a.send(2)
print(r)
r = a.send(2)
print(r)

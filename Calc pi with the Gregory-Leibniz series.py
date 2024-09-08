pi = 0
y = 1
numerater = 4
while True:
    pi = pi + numerater/y
    y = (y + 2) * -1
    print(pi)
    pi = pi + numerater/y
    y = (y - 2) * -1
    print(pi)
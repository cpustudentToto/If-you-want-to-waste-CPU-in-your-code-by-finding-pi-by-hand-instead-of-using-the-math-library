pi = 3
y = 2
numerater = 4
while True:
    pi = pi + numerater/((y)(y+1)(y+2))
    y = (y + 2) * -1
    print(pi)
    pi = pi + numerater/((y)(y+1)(y+2))
    y = (y - 2) * -1
    print(pi)
x = 10
y = 3
def calculs(x,y):
    for i in range(1, 5):
        if x > y:
            x = x / 2 + 1
            y = y + 1
        else:
            x = x + i
            y = y / 2 + i
    print(x, y)

print(calculs(x,y))

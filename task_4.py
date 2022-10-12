import math

def snowball(n, k):
    radius = n / 2 # also centre coordinates

    for i in range(n): # y
        line = " " * k

        for j in range(n): # x

            if math.sqrt(((j + 0.5) - radius) ** 2 + ((i + 0.5) - radius) ** 2) <= radius:
                line += "#"

            else:
                line += " "

        print(line)


def snowman(n):
    snowball(n, 2)
    snowball(n+2, 1)
    snowball(n+4, 0)

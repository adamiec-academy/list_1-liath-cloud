def cross(n):
    def cross(n):
    up_and_down = " " * n + "*" * n + " " * n
    middle = "*" * 3 * n

    for i in range(0, n * 3):
        if i < n or  i >= 2 * n:
            print(up_and_down)
        else:
            print(middle)

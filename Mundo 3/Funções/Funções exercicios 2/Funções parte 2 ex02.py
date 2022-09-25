def fatorial(n):
    f = 1
    for i in range(n, 0, -1):
        print(i, end=" ")
        if i > 1:
            print("x", end=" ")
        else:
            print("=", end=" ")
        f *= i
    print(f)


fatorial(5)

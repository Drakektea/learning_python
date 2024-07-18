def F(n):
    if n < 1:
        return 0
    elif n < 3:
        return 1
    return F(n - 1) + F(n - 2)


print(F(40))

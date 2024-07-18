def f(n):
    if n < 1:
        return
    print(n)
    f(n - 1)
    print(f'{n} цикл рекурсии закончен!')


f(100)

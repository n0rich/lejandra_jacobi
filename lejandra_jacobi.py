import timeit


def pfacs(n):
    # факторизация
    i = 2
    pfac = []
    while i * i <= n:
        while n % i == 0:
            pfac.append(int(i))
            n = n / i
        i = i + 1
    if n > 1:
        pfac.append(int(n))
    return pfac


def leandra(a, b):
    # вычисление символа Лежандра
    res = []
    if a > 0:
        a = a % b
    fac_a = pfacs(a)
    for num in fac_a:
        if num == 2:
            r = -1 ** (((b ** 2) - 1) / 8)
        else:
            r = -1 ** (((b - 1) / 2) * ((num - 1) / 2) * leandra(b, num))
        res.append(r)
    result = 1
    for r in res:
        result = result * r
    return result


def jacobi(a, b):
    # вычисление символа Якоби
    fac_b = pfacs(b)
    result = 1
    for num in fac_b:
        result = result * leandra(a, num)
    return result


print("Данная программа считает символ Лежандра и символ Якоби.")
while True:
    print("Для расчета символа Лежандра введите 'l'")
    print("Для расчета символа Якоби введите 'j'")
    print("Для выхода введите 'q'")
    symbol = input()
    if symbol == 'q':
        break
    a = input("Введите число a: ")
    b = input("Введите число p: ")
    if symbol == 'l':
        start = timeit.default_timer()
        print("Символ Лежандра равен: " + str(leandra(int(a), int(b))))
        stop = timeit.default_timer()
        execution_time = stop - start
        print("Время вычисления: " + str(execution_time))
    elif symbol == 'j':
        start = timeit.default_timer()
        print("Символ Якоби равен: " + str(jacobi(int(a), int(b))))
        stop = timeit.default_timer()
        execution_time = stop - start
        print("Время вычисления: " + str(execution_time))
    else:
        print("НЕКОРРЕКТНЫЙ СИМВОЛ")

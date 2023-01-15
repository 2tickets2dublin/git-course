import time


def get_nod(a, b):
    """Вычисляется НОД для двух натуральных чисел a и b
    по быстрому алгоритму Евклида.

    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


def test_nod(func):
    # test number 01
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print("test 01 is successful")
    else:
        print("test 01 is failed")
    # test number 02
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print("test 02 is successful")
    else:
        print("test 02 is failed")
    # test number 03 speed
    a = 2
    b = 100000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print("test 03 speed is successful")
    else:
        print("test 03 speed is failed")
    print(dt)

test_nod(get_nod)

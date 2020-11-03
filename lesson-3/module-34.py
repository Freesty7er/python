def my_func(x,y):
    res = 1

    for i in range(abs(y)):
        res *= 1/x
    return res

try:
    x = float(input("введите действительное положительное число: "))
    y = int(input("введите целое отрицательное число: "))

    if x > 0 and y<0:
        print(f"результат возведения в степень: {my_func(x,y)}")
    else:
        print("х - должен быть положительным, а у - отрицательным")
except ValueError:
    print("Value error")


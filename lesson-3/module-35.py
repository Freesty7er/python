def my_func(arg_1):

    global summa

    result = True

    for i,j in enumerate(arg_1):
        if j == "*":
            result = False
            break
        else:
            summa += float(j)

    print(f"сумма = {summa}")


    return result

# ----------------------------------------------------------------------------------------------------------------------
summa = 0;

i = True
while i:

    my_str = input("введите числа разделенные пробелом. '*' - завершение: ")

    i = my_func(my_str.split())



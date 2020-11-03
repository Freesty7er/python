def my_func(arg_1, arg_2):
    if arg_2 == 0:
        print("деление на ноль")
    else:
        print(f"результат деления {arg_1/arg_2}")

my_num1 = float(input("введите первое число: "))
my_num2 = float(input("введите второе число: "))

my_func(my_num1, my_num2)
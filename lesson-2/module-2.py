my_str = input("Введите значения разделенные пробелом: ")
my_list = list(my_str.split())

for i in range(len(my_list)):
    if i%2 != 0:
        my_list[i-1], my_list[i] = my_list[i], my_list[i-1]

print(my_list)
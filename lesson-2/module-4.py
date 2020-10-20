my_str = input("Введите несколько слов разделенных пробелами: ")

my_list = list(my_str.split())

for i,j in enumerate(my_list):
    print(str(i+1) + " " + j[:10])
my_str = input("Введите номер месяца (целое число): ")

my_list = ["зима"]*3 + ["весна"]*3 + ["лето"]*3 + ["осень"]*3
my_dict = {1:"зима",2:"зима",3:"весна",4:"весна",5:"весна",6:"лето",7:"лето",8:"лето",9:"осень",10:"осень",11:"осень",12:"зима"}

my_number = int(my_str)
if my_number > 0 & my_number < 13:
    print("list")
    print("-"*12)
    print(my_list[my_number-12])

    print("")

    print("dict")
    print("-"*12)
    print(my_dict.get(my_number))
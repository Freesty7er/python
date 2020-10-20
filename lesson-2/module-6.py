my_list = []
my_num_id = 1


while True:

    my_str_act = input("\n 1 - добавить товар\n 2 - показать список\n 3 - показать аналитику\n 4 - завершить\n")

    if my_str_act == "1":

        my_str_name = input("Введите Наименование товара: ")
        my_str_price = input("Введите Цену товара: ")
        my_str_qty = input("Введите Количество товара: ")
        my_str_unit = input("Введите Ед. измерения товара: ")

        my_list.append((my_num_id, {"название":my_str_name, "цена":float(my_str_price), "количество":float(my_str_qty), "ед":my_str_unit}))
        my_num_id += 1

    elif my_str_act == "2":

        print(my_list)

    elif my_str_act == "3":

        my_dict = {"название": [], "цена": [], "количество": [], "ед": []}

        for i in range(len(my_list)):

            for i,j in enumerate(my_list[i][1].items()):

                my_dict[j[0]].append(j[1])

        print(my_dict)

    else:
        break
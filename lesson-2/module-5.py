my_list = [7,5,3,3,2]


while True:
    my_str = input("Введите натуральное число включая ноль (пустая строка прекратить ввод): ")
    if my_str == "":
        break
    else:
        my_num = int(my_str)

    num_inserted = False

    for i in range(len(my_list)):
        #print(my_list[i])
        if my_num > my_list[i]:
            my_list.insert(i, my_num)
            num_inserted = True
            break
    if num_inserted == False:
        my_list.append(my_num)

    print(my_list)
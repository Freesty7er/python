int_number = int(input("enter int number"))
max_number = 0

while int_number > 0:
    k = int_number % 10

    if k > max_number:
        max_number = k

    int_number = int_number // 10

print("max number %d"%max_number)
int_number = int(input("enter int number"))
max_number = 0

while int_number > 0:
    k = int_number % 10

    if k > max_number:
        max_number = k

    int_number = int_number // 10

print("max number %d"%max_number)
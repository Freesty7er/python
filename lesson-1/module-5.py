v = float(input("введите выручку"))
i = float(input("введите издержки"))

f = v - i

if f > 0:
    print("прибыль")

    r = f/v
    print(f"рентабельность: {r}")

    s = int(input("введите численность сотрудников:"))

    if s > 0:
        print(f"рентабельность на сотрудника: {r/s}")

elif f < 0:
    print("убыток")

v = float(input("введите выручку"))
i = float(input("введите издержки"))

f = v - i

if f > 0:
    print("прибыль")

    r = f/v
    print(f"рентабельность: {r}")

    s = int(input("введите численность сотрудников:"))

    if s > 0:
        print(f"рентабельность на сотрудника: {r/s}")

elif f < 0:
    print("убыток")


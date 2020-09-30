n = input("enter number")

arg_1 = int(n)
arg_2 = int(format("%s%s"%(n,n)))
arg_3 = int(format("%s%s%s"%(n,n,n)))

print(f"{arg_1 + arg_2 + arg_3}")

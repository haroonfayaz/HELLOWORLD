weight = int(input ("what is your weight "))
unit  = input("(L)s or (K)s")
if unit.upper() == "L":
    converted = weight *.45
    print (f"you are {converted} kilos ")
else:
    converted = weight /.45
    print(f"you are {converted} pounds")

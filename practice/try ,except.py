try:
    age =int(input(print("enter your age ")))
    income = 200000
    result = income /age
    print(result)
except ZeroDivisionError :
   print("can't divide with zero")
except ValueError:
    print("only type numerals")
n = int(input().strip())
if n % 2 != 0 :
    print ("n is odd and odd numbers are  wierd")
elif n % 2 == 0 and n in range (2,6):
    print ("n is even and is not weird")
elif n in range (6,20):
    print("n is even and is weird")
elif n >20 :
    print("n is evem and is not weird")

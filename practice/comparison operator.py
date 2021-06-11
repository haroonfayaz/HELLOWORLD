name = (input("enter your name "))
length = len(name)

if length <= 3:
     print("name too short,type atleast 4")
elif length >= 50 :
     print("name too long ")
else:
     print("name is ok")

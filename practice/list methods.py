numbers =[2,2,2,3,3,3,4,4,4,5,5,5,5,6,6,6,7,7,7,7]
uniques =[]
print(len(numbers))
for number in numbers :
    if number not in uniques:
        uniques.append(number)
print(uniques)
print(len(uniques))
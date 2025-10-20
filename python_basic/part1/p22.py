def counter(list1):
    count4=0
    for n in list1:
        if n ==4:
            count4 +=1

    return count4
    
print(counter([1,2,4,5,6,7,]))
print(counter([1,2,4,5,4,4,]))
def histogram(list1):
    for n in list1:
        str1 = ''
        times = n
        
        while times > 0:
            str1 += '*'
            times = times - 1

        print(str1)

histogram([3,5,7,2,7])

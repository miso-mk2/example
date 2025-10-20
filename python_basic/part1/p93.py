num1 =1
str1 ="hello"
lst1 =[1,2,3]

def kansu(arg1):
    print(f"id={id(arg1)}")
    print(f"型={type(arg1)}")
    print(f"値={arg1}")
    
kansu(num1)
kansu(str1)
kansu(lst1)
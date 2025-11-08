class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        for i0 in range(2):
            num1_int=0
            
            if i0 ==0:
                str1=num1
            else:
                str1=num2

            for i1 in range(len(str1)):
                
                num1_int *= 10
                if str1[i1]=="1":
                    num1_int += 1
                if str1[i1]=="2":
                    num1_int += 2
                if str1[i1]=="3":
                    num1_int += 3
                if str1[i1]=="4":
                    num1_int += 4
                if str1[i1]=="5":
                    num1_int += 5
                if str1[i1]=="6":
                    num1_int += 6
                if str1[i1]=="7":
                    num1_int += 7
                if str1[i1]=="8":
                    num1_int += 8
                if str1[i1]=="9":
                    num1_int += 9
                if str1[i1]=="0":
                    num1_int += 0
                print(num1_int)

            else:
                print("end")
                if i0 ==0:
                    num3=num1_int
                else:
                    num4=num1_int
        
        return str(num3*num4)

hoge=Solution()
print(hoge.multiply("12","3"))

"""
文字列型の非負整数ふたつを”直接整数に変換しないで”掛け算して、文字列で返せ
最大200桁 先頭にゼロは含まれない


"""
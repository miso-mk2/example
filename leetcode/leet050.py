class Solution:
    def myPow(self, x: float, n: int) -> float:

        output = 1
        num1 = abs(n)
    
        # *xをn回繰り返す奴だと時間切れになるので、
        # nを2進数として、一個前の計算結果をx*=xすることで掛け算の回数を減らす
        while num1 > 0:
            if num1 % 2 == 1:
                output *= x
            
            x *= x
            num1 //= 2
        
        #マイナスの場合
        return output if n > 0 else 1/output
    
hoge=Solution()

print(hoge.myPow(2.00000,10))
print(hoge.myPow(2.00000,-2))

"""
xのn乗を計算しろ

1:42

"""
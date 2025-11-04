class Solution:
	def generateParenthesis(self, n: int) -> list[str]:
		
		if n==1:
			return ["()"]

		output = []
		keta = (n-1)*2
		
		#二進数のリストを生成
		lst1 = [
        	format(i, 'b').zfill(keta)
        	for i in range(2**keta)
    	]
		#リスト要素を確認
		for	i in lst1:

			count0 = 0
			count1 = 0

			#二進数文字列を頭から確認
			for j in i:

				#1と0の個数をカウント
				if j == "1":
					count1 +=1
				else:
					count0 +=1

				#閉じ括弧が先に来すぎならbreak
				if count0 > count1+1:
					break

			#開き括弧と閉じ括弧の個数が一致なら合格
			if count0 == count1:
				str1 = i.replace("1","(")
				str1 = str1.replace("0",")")
				str1 = "(" + str1 + ")"
				output.append(str1)

		return output





hoge=Solution()
print(hoge.generateParenthesis(3))

"""
n個の括弧で作れるパターンを全パターン作れとのこと
１なら ()
２なら ()() と (())
３なら ()()() と ((())) と (())() と ()(()) と (()())

nは最大8

format(変数,"b")
	指定の変数をバイナリに変換
.zfill()
	str型メソッド 指定桁で０埋め

"""
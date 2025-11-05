class Solution:
	def nextPermutation(self, nums: list[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		#print(f"開始={nums}")

		for i1 in range(len(nums)-1):
			#比較対象の最前項
			sentou = nums[-i1-2]
			#最前項より後ろの要素リスト
			lst1 = nums[-i1-1:]
			#際前項より大きい要素リスト
			lst2 = [x for x in lst1 if x > sentou]

			#print(f" sentou={sentou}\n lst1={lst1}\n lst2={lst2}")
			
			#大きい要素がないならcontinue
			#あったなら際前項に入れ替え
			if len(lst2)==0:
				continue
			else:
				#最前項より大きい一番小さい数を最前項に入れる
				nums[-i1-2] = min(lst2)

				#際前項より後ろの要素リストに旧最前項を追加＆新最前項削除して逆順ソート
				lst1.append(sentou)
				lst1.remove(nums[-i1-2])
				lst1.sort(reverse=True)
				#含めた全要素を後ろから大きい順に入れる（前に行くほど小さい）
				for i2 in range(len(lst1)):
					#print(f"逆順={lst1[i2]}")
					nums[-i2-1] = lst1[i2]
				break
		else:
			#見つからなかった場合はソートして返す
			nums.sort()
			
		#print(f"結果={nums}")

		"""		
		判定範囲内の最前項より大きい、最前項以外の中で一番小さい数字を最前項に入れる
		最前項が最も大きい場合は判定範囲を拡大しもう一度↑
		最前項が確定したら残りの数字を小さい順にソートして入れる
		"""
		return


hoge=Solution()
print(hoge.nextPermutation([2,3,1]))

"""
「次の順列」
例）
1と2と3のリストが渡された場合、
その三つの数字で出せる順列は、「先頭が小さい順」だと
1,2,3 1,3,2 2,1,3 2,3,1 3,1,2 3,2,1
  ↑	    ↑
となる
で、これの次の順列に変更しろとのこと
1,2,3が渡されたら1,3,2に変更する

出力ではなく、リストの中身を書き換えるだけ
（リスト型はミュータブルなので関数内での書き換えが反映される）

"""
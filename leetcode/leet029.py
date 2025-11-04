class Solution:
	def divide(self, dividend: int, divisor: int) -> int:

		is_minus = True if (dividend < 0) ^ (divisor < 0) else False
		dividend = abs(dividend)
		divisor	= abs(divisor)

		output=0
		while dividend >= divisor:
			if dividend >= divisor*1000:
				dividend -= divisor*1000
				output += 1000
			elif dividend >= divisor*100:
				dividend -= divisor*100
				output += 100
			elif dividend >= divisor*10:
				dividend -= divisor*10
				output += 10
			else:
				dividend -= divisor
				output += 1

			if 2**31-1 <= output and not is_minus:
				break
			if 2**31 <= output:
				break

		if is_minus:
			output *= -1

		return output


hoge=Solution()
print(hoge.divide(-2147483648,-1))

"""
乗算除算modを使わずに割り算をする問題

切り捨てで整数除算
マイナスはあり
32ビット範囲内に収める

"""
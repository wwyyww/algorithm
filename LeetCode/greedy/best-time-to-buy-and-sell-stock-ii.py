#122. Best Time to Buy and Sell Stock II
#문제 링크 : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

#내 풀이
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit=0
        for i in range(0, len(prices)-1):
            if prices[i]<prices[i+1]:
                profit+=prices[i+1]-prices[i]
                
                
        return profit

'''
같은날 팔고 구매도 할 수 있기 때문에 다음 가격이 이전 가격보다 높으면 빼서 결과에 더해주었다.
'''

#책 풀이 : 파이썬다운 방식
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0보다 크면 무조건 합산
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

'''
이익이 0보다 크면 무조건 합하게 한다.
'''
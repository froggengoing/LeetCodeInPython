# You are given an array prices where prices[i] is the price of a given stock on
#  the ith day. 
# 
#  You want to maximize your profit by choosing a single day to buy one stock an
# d choosing a different day in the future to sell that stock. 
# 
#  Return the maximum profit you can achieve from this transaction. If you canno
# t achieve any profit, return 0. 
# 
#  
#  Example 1: 
# 
#  
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 
# 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must
#  buy before you sell.
#  
# 
#  Example 2: 
# 
#  
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= prices.length <= 105 
#  0 <= prices[i] <= 104 
#  
#  Related Topics Array Dynamic Programming 
#  👍 10027 👎 403


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def maxProfit(self, prices):
        '''
        动态规划
        求当前元素左边最小值与当前值之差
        '''
        left_min = [prices[0]]
        max_value = 0
        for i in range(1, len(prices)):
            left_min.append(min(prices[i - 1], left_min[i - 1]))
            max_value = max(prices[i] - left_min[i], max_value)
        return max_value

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_value = prices[0]
        res = 0
        for index in range(1, len(prices)):
            if prices[index] < min_value:
                min_value = prices[index]
            else:
                res = max(prices[index] - min_value, res)
        return res

        # leetcode submit region end(Prohibit modification and deletion)


s1 = Solution()
print(s1.maxProfit([7, 3, 5, 2, 1, 4]))
print(s1.maxProfit([1, 7, 6, 4, 3, 1]))
print(s1.maxProfit([7, 1, 5, 3, 6, 4]))

print(s1.maxProfit2([7, 3, 5, 2, 1, 4]))
print(s1.maxProfit2([1, 7, 6, 4, 3, 1]))
print(s1.maxProfit2([7, 1, 5, 3, 6, 4]))

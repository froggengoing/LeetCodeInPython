# Alice and Bob play a game with piles of stones. There are an even number of pi
# les arranged in a row, and each pile has a positive integer number of stones pil
# es[i]. 
# 
#  The objective of the game is to end with the most stones. The total number of
#  stones across all the piles is odd, so there are no ties. 
# 
#  Alice and Bob take turns, with Alice starting first. Each turn, a player take
# s the entire pile of stones either from the beginning or from the end of the row
# . This continues until there are no more piles left, at which point the person w
# ith the most stones wins. 
# 
#  Assuming Alice and Bob play optimally, return true if Alice wins the game, or
#  false if Bob wins. 
# 
#  
#  Example 1: 
# 
#  
# Input: piles = [5,3,4,5]
# Output: true
# Explanation: 
# Alice starts first, and can only take the first 5 or the last 5.
# Say she takes the first 5, so that the row becomes [3, 4, 5].
# If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 poi
# nts.
# If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win wi
# th 9 points.
# This demonstrated that taking the first 5 was a winning move for Alice, so we 
# return true.
#  
# 
#  Example 2: 
# 
#  
# Input: piles = [3,7,2,3]
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= piles.length <= 500 
#  piles.length is even. 
#  1 <= piles[i] <= 500 
#  sum(piles[i]) is odd. 
#  
#  Related Topics Array Math Dynamic Programming Game Theory 
#  👍 1576 👎 1737


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        res = [[None for i in range(len(piles))] for i in range(len(piles))]
        score = self.dfs(piles, res, 0, len(piles) - 1)
        print(res)
        return score > 0

    def dfs(self, nums, res, i, j):
        if i > j:
            return 0
        #     return None
        # elif i == j:
        #     res[i][j] = nums[i]
        elif res[i][j]:
            return res[i][j]
        else:
            res[i][j] = max(nums[i] - self.dfs(nums, res, i + 1, j),
                            nums[j] - self.dfs(nums, res, i, j - 1))
        return res[i][j]

# leetcode submit region end(Prohibit modification and deletion)
'''
[[1, 1, 2, 2], 
[N, 2, 1, 3], 
[N, N, 3, 1], 
[N, N, N, 4]]
'''
print(Solution().stoneGame([1,2,3,4]))
# print(5-None)
# 偶数，偶数下先手必胜，
# 最简单的理解是先手可以一直拿偶数或者奇数，
# 只要计算出奇偶哪个最大就可以。
# 但这里不是最优解，也就是不能得到最大净胜分
# 反过来理解486，奇数情况下，我先拿了一个，剩下是偶数，也就是对手一定概率下必胜。
# 除非对手在偶数必胜条件下的净胜分没有我先拿的这个大
# Alice and Bob continue their games with piles of stones. There are a number of
#  piles arranged in a row, and each pile has a positive integer number of stones 
# piles[i]. The objective of the game is to end with the most stones. 
# 
#  Alice and Bob take turns, with Alice starting first. Initially, M = 1. 
# 
#  On each player's turn, that player can take all the stones in the first X rem
# aining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). 
# 
#  The game continues until all the stones have been taken. 
# 
#  Assuming Alice and Bob play optimally, return the maximum number of stones Al
# ice can get. 
# 
#  
#  Example 1: 
# 
#  
# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, t
# hen Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If A
# lice takes two piles at the beginning, then Bob can take all three piles left. I
# n this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larg
# er. 
#  
# 
#  Example 2: 
# 
#  
# Input: piles = [1,2,3,4,5,100]
# Output: 104
#  
# 
#  
#  Constraints: 
# [2,7,9,4,4]
# [2,7,9,8,4]
# [2,7,9,8,4]
# [2,7,9,8,4]
# [2,7,9,8,4]
# [2,7,9,8,4]
#
# [[9, 22, 26, 26, 26],
# [16, 24, 24, 24, 24],
# [13, 17, 17, 17, 17],
# [8, 8, 8, 8, 8],
# [4, 4, 4, 4, 4]]
# [[0, 0, 0, 0, 0],
# [10, 16, 13, 8, 4],
# [22, 24, 17, 8, 4],
# [26, 24, 17, 8, 4],
# [26, 24, 17, 8, 4],
# [26, 24, 17, 8, 4]]
#
#  1 <= piles.length <= 100 
#  1 <= piles[i] <= 104 
#  
#  Related Topics Array Math Dynamic Programming Game Theory 
#  👍 1001 👎 225


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        res = [[0 for i in range(len(piles))] for i in range(len(piles) + 1)]
        sum = 0
        for i in range(len(piles) - 1, -1, -1):
            sum += piles[i]
            for m in range(1, len(piles) + 1):
                if i + 2 * m >= len(piles):
                    res[m][i] = sum
                else:
                    for x in range(1, 2 * m + 1):
                        res[m][i] = max(res[m][i], sum - res[max(x, m)][i + x])

        # print(res)
        return res[1][0]


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().stoneGameII([2, 7, 9, 4, 4]))
print(Solution().stoneGameII([1, 1, 1, 2, 2, 2]))

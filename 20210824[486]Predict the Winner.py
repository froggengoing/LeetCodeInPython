# You are given an integer array nums. Two players are playing a game with this 
# array: player 1 and player 2. 
# 
#  Player 1 and player 2 take turns, with player 1 starting first. Both players 
# start the game with a score of 0. At each turn, the player takes one of the numb
# ers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which 
# reduces the size of the array by 1. The player adds the chosen number to their s
# core. The game ends when there are no more elements in the array. 
# 
#  Return true if Player 1 can win the game. If the scores of both players are e
# qual, then player 1 is still the winner, and you should also return true. You ma
# y assume that both players are playing optimally. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,5,2]
# Output: false
# Explanation: Initially, player 1 can choose between 1 and 2. 
# If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If playe
# r 2 chooses 5, then player 1 will be left with 1 (or 2). 
# So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
# Hence, player 1 will never be the winner and you need to return false.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,5,233,7]
# Output: true
# Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 a
# nd 7. No matter which number player 2 choose, player 1 can choose 233.
# Finally, player 1 has more score (234) than player 2 (12), so you need to retu
# rn True representing player1 can win.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 20 
#  0 <= nums[i] <= 107 
#  
#  Related Topics Array Math Dynamic Programming Recursion Game Theory 
#  👍 2271 👎 123


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def PredictTheWinner2(self, nums):
        '''
        网友提供的第二种思路更好理解，但是存在重复运算，效率低
        :param nums:
        :return:
        '''
        return self.dfs2(nums, 0, len(nums) - 1) >= 0

    def dfs2(self, nums, i, j):
        '''
        理解为当前玩家能拿到的最大净胜分
        '''
        if (i == j): return nums[i]
        if (i > j): return 0
        # 当前玩家选择了元素i，则对手会选择剩下元素的最优解，剩下的元素最终体现为净胜分
        r = nums[i] - self.dfs2(nums, i + 1, j)
        l = nums[j] - self.dfs2(nums, i, j - 1)
        return max(r, l)

    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        [[1, 4, -2, 6, 0],
        [N, 5, 3, 3, 3],
        [N, N, 2, 2, 4],
        [N, N, N, 4, 2],
        [N, N, N, N, 6]]
        从当前玩家总是拿最优结果来说：
        先看局部：
            斜边意味这i=j，此时只剩一个数据，所以玩家总是拿nums[i]
            如下：[0][1]=2 表示当前轮中，选手一定从最优角度出发，从2和4中选，一定是选择4，而另一个选择2，所以净胜分为2
            [2][3]=2 ，同理，在当前论中从最优角度出发，一定选择6，净胜分为2
            [0][3]=4，表示选手1可能
                    选择一：nums[0],那么选手2肯定会拿nums[1],nums[2]的最优解，即净胜分为2，净胜分可视为选手2选择的元素，
                        此时nums[0]- score(2) = 0,即平手
                    选择二：nums[2],选手2选择最优解后最终得分是2，此时选手一净胜分6-2 = 4
            所以[0][3]表示选手1最大净胜分为4
            [2, 2, 4]
            [N, 4, 2]
            [N, N, 6]
        """
        # res = [[None] * len(nums)] * len(nums)
        res = [[None for i in range(len(nums))] for j in range(len(nums))]
        score = self.dfs(nums, 0, len(nums) - 1, res)
        # print(res)
        return score >= 0

    def dfs(self, nums, i, j, res):
        if i > j:
            return 0
        if res[i][j]:
            return res[i][j]
        res[i][j] = max(nums[i] - self.dfs(nums, i + 1, j, res),
                        nums[j] - self.dfs(nums, i, j - 1, res))
        return res[i][j]


# leetcode submit region end(Prohibit modification and deletion)
# print(Solution().PredictTheWinner([1, 5, 9, 6]))
print(Solution().PredictTheWinner([1, 5, 2, 4, 6]))
# print(Solution().PredictTheWinner( [2,4,55,6,8] ))

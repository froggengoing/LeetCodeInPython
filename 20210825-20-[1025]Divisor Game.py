# Alice and Bob take turns playing a game, with Alice starting first. 
# 
#  Initially, there is a number n on the chalkboard. On each player's turn, that
#  player makes a move consisting of: 
# 
#  
#  Choosing any x with 0 < x < n and n % x == 0. 
#  Replacing the number n on the chalkboard with n - x. 
#  
# 
#  Also, if a player cannot make a move, they lose the game. 
# 
#  Return true if and only if Alice wins the game, assuming both players play op
# timally. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: true
# Explanation: Alice chooses 1, and Bob has no more moves.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3
# Output: false
# Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
#  
# n = 4
# Alice choose f(1), !f(4-1)
# return true
# Alice choose f(2), !f(2)
# return false
#
# n = 5
# Alice choose f(1), !f(5-1)
# return false
# n =6
# Alice choose f(1), !f(6-1)
# return True
# Alice choose f(2), !f(6-2)
# return false
# Alice choose f(3), !f(6-3)
# return true
#
#
#
#  Constraints:
# 
#  
#  1 <= n <= 1000 
#  
#  Related Topics Math Dynamic Programming Brainteaser Game Theory 
#  👍 975 👎 2502


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def divisorGame(self, n):
        '''

        :param n:
        :return:
        '''
        return n % 2 == 0

    def divisorGame3(self, n):
        res = [None] * n
        self.def3(res, 0)
        return res[n - 1]

    def def3(self, res, i):
        if i >= len(res):
            return False
        if i == 0:
            res[0] = False
        elif i == 1:
            res[1] = True
        elif i == 2:
            res[2] = False
        elif res[i] == False:
            return res[i]
        else:
            tmp = 1
            while tmp < i:
                if (i + 1) % tmp == 0 and res[i - tmp] == False:
                    res[i] = True
                    break
                tmp += 1
            if res[i] == None:
                res[i] = False
        self.def3(res, i + 1)

    def divisorGame2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1: return False
        if n == 2: return True
        if n == 3: return False
        res = [None] * n
        res[0] = False
        res[1] = True
        res[2] = False
        i = 3
        while i < n:
            self.dfs2(res, i)
            i += 1
        return res[n - 1]

    def dfs2(self, res, i):
        tmp = 1
        while tmp < i:
            if (i + 1) % tmp == 0 and res[i - tmp] == False:
                res[i] = True
                return
            tmp += 1
        res[i] = False

    # leetcode submit region end(Prohibit modification and deletion)


for i in range(1, 10):
    print(Solution().divisorGame(i))

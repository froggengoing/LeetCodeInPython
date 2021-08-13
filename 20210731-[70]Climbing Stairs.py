# You are climbing a staircase. It takes n steps to reach the top. 
# 
#  Each time you can either climb 1 or 2 steps. In how many distinct ways can yo
# u climb to the top? 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 45 
#  
#  Related Topics Math Dynamic Programming Memoization 
#  👍 7471 👎 227


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def climbStairs(self, n):
        '''
        斐波那契数列。实际上我们只需要前两个值，所以保存前两个值就好了
        时间：o(n)
        空间：o(1)
        '''
        res = 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        first = 1
        sec = 2
        index = 3
        while index <= n:
            res = first + sec
            first = sec
            sec = res
            index += 1
        return res

    def climbStairs4(self, n):
        '''
        斐波那契数列
        时间：o(n)
        空间：o(n)
        '''
        his = [0] * n
        index = 0
        while index < n:
            if index == 0:
                his[0] = 1
            elif index == 1:
                his[1] = 2
            else:
                his[index] = his[index - 1] + his[index - 2]
            index += 1
        return his[n - 1]


    '''
    网友的精简写法，但本质还是递归
    '''


    def climb(self, n):
        return self.climb(n - 1) + self.climb(n - 2) if n > 2 else 2 if n == 2 else 1


    '''
    对方式2的优化，递归一般使用数组保存历史计算的值
    '''


    def climbStairs3(self, n):
        his = [0] * n
        return self.doClimbStairs3(0, n, his)


    def doClimbStairs3(self, i, n, his):
        if i > n:
            return 0
        if i == n:
            return 1
        if his[i] > 0:
            return his[i]
        his[i] = self.doClimbStairs3(i + 1, n, his) + self.doClimbStairs3(i + 2, n, his)
        return his[i]


    '''
    题目最直白的理解如下：
                                  0,5
                   1,5                                  2.5
              2,5               3,5                3,5        4,5
       3,5        4,5        4,5     5,5       4,5  5,5     5,5  6，5
    4,5    5,5    5,5  6，5   5,5  6，5         5,5  6，5
    5,5  6，5
    思路很清晰，考虑递归累加。
    问题是，这种方式会导致调用栈过深，可能栈溢出。这里n=38时，无法输出结果
    '''


    def climbStairs2(self, n):
        return self.doClimbStairs2(0, n)


    def doClimbStairs2(self, i, n):
        if (i > n):
            return 0
        if (i == n):
            return 1
        return self.doClimbStairs2(i + 1, n) + self.doClimbStairs2(i + 2, n)


    ## 第一次提交
    # 时间复杂度为 n^2
    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = n // 2
        cur = 0
        res = 0
        while cur <= k:
            res += self.count(n, cur)
            cur += 1
        return res


    def count(self, n, k):
        if n == k:
            return 1
        if k == 0:
            return 1
        count_1 = n - k * 2 + k
        up_sum = 1
        cur = count_1
        while True:
            up_sum *= cur
            if count_1 - cur + 1 >= k:
                break
            cur -= 1
        div_sum = 1
        div_cur = k
        while True:
            div_sum *= div_cur
            if div_cur <= 1:
                break
            div_cur -= 1
        return up_sum // div_sum


# leetcode submit region end(Prohibit modification and deletion)
s1 = Solution()
print(s1.climbStairs(10))


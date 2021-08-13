# Given an array of integers temperatures represents the daily temperatures, ret
# urn an array answer such that answer[i] is the number of days you have to wait a
# fter the ith day to get a warmer temperature. If there is no future day for whic
# h this is possible, keep answer[i] == 0 instead. 
# 
#  
#  Example 1: 
#  Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
#  Example 2: 
#  Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
#  Example 3: 
#  Input: temperatures = [30,60,90]
# Output: [1,1,0]
#  
#  
#  Constraints: 
# 
#  
#  1 <= temperatures.length <= 105 
#  30 <= temperatures[i] <= 100 
#  
#  Related Topics Array Stack Monotonic Stack 
#  👍 4825 👎 138


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        单调栈
        """
        length = len(temperatures)
        stack = [length - 1]
        res = [0] * length
        for i in range(length - 2, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res


# leetcode submit region end(Prohibit modification and deletion)
s1 = Solution()
print(s1.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(s1.dailyTemperatures([30, 40, 50, 60]))
print(s1.dailyTemperatures([30, 60, 90]))
# 测试结果:                  [8,1,5,4,1,2,1,1,0,0]
# 期望结果:[8,1,5,4,3,2,1,1,0,0]
print(s1.dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))

# Given n non-negative integers representing an elevation map where the width of
#  each bar is 1, compute how much water it can trap after raining. 
# 
#  
#  Example 1: 
# 
#  
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [
# 0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are
#  being trapped.
#  
# 
#  Example 2: 
# 
#  
# Input: height = [4,2,0,3,2,5]
# Output: 9
#  
# 
#  
#  Constraints: 
# 
#  
#  n == height.length 
#  1 <= n <= 2 * 104 
#  0 <= height[i] <= 105 
#  
#  Related Topics Array Two Pointers Dynamic Programming Stack Monotonic Stack 
#  👍 13247 👎 190


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def trap(self, height) -> int:
        '''
        单调栈
        :param height:
        :return:int
        '''
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                cur = stack.pop()
                if not stack: break
                res += (min(height[stack[-1]], height[i]) - height[cur]) * (i - stack[-1] - 1)
            stack.append(i)
        return res

    def trap2(self, height):
        """
        :type height: List[int]
        :rtype: int
        解法一 单调堆的思路 变种
        算不出来/(ㄒoㄒ)/~~
        """
        length = len(height)
        # 初始化
        index = 1
        total = 0
        while index < length:
            jndex = index - 1
            if height[jndex] < height[index]:
                while jndex >= 0 and height[jndex] < height[index]:
                    jndex -= 1
                if jndex != -1:
                    # 判断该层填充大小
                    min_height = min(height[jndex], height[index])
                    total += (index - jndex - 1) * (min_height - height[index - 1])
            index += 1
        return total


# leetcode submit region end(Prohibit modification and deletion)
s1 = Solution()
# print(s1.trap([4, 2, 0, 3, 2, 5]))
print(s1.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

# Given a circular integer array nums (i.e., the next element of nums[nums.lengt
# h - 1] is nums[0]), return the next greater number for every element in nums. 
# 
#  The next greater number of a number x is the first greater number to its trav
# ersing-order next in the array, which means you could search circularly to find 
# its next greater number. If it doesn't exist, return -1 for this number. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number. 
# The second 1's next greater number needs to search circularly, which is also 2
# .
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 104 
#  -109 <= nums[i] <= 109 
#  
#  Related Topics Array Stack Monotonic Stack 
#  👍 3065 👎 103


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [-1] * len(nums)
        i = 0
        is_second = False
        # 优化 是 2* len(nums) -1
        # 下表为i%len(nums)取模
        # 即作为[2n-1]的数组
        while i < len(nums):
            while stack and nums[i] > nums[stack[-1]]:
                result[stack.pop()] = nums[i]
            stack.append(i)
            i += 1
            if i == len(nums) and not is_second:
                i = 0
                is_second = True
        return result


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().nextGreaterElements([1, 2, 3, 4, 3, 2]))
print(Solution().nextGreaterElements([1, 2, 1]))

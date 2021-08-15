# Given an integer array nums, you need to find one continuous subarray that if 
# you only sort this subarray in ascending order, then the whole array will be sor
# ted in ascending order. 
# 
#  Return the shortest such subarray and output its length. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the 
# whole array sorted in ascending order.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3,4]
# Output: 0
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 104 
#  -105 <= nums[i] <= 105 
#  
# 
#  
# Follow up: Can you solve it in O(n) time complexity? Related Topics Array Two 
# Pointers Stack Greedy Sorting Monotonic Stack 
#  👍 4247 👎 189


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        双单调栈，求出左右两侧不需要调整位置的索引值
        """
        left_stack = []
        right_stack = []
        min_index = len(nums)
        # max_index = 0
        max_index = len(nums)
        for i in range(len(nums)):
            while left_stack and nums[left_stack[-1]] > nums[i]:
                left_stack.pop()
                min_index = min(len(left_stack), min_index)
            left_stack.append(i)
        for i in range(len(nums) - 1, -1, -1):
            while right_stack and nums[right_stack[-1]] < nums[i]:
                right_stack.pop()
                max_index = min(len(right_stack), max_index)
                # max_index = max(len(nums) - len(right_stack) - 1, max_index)
            right_stack.append(i)
        max_index = len(nums) - max_index - 1
        if max_index > min_index:
            return max_index - min_index + 1
        return 0
        # leetcode submit region end(Prohibit modification and deletion)


s1 = Solution()

print(s1.findUnsortedSubarray([1, 3, 2, 2, 2]))
print(s1.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print(s1.findUnsortedSubarray([1, 2, 3, 4]))
print(s1.findUnsortedSubarray([4, 3, 2, 1]))
print(s1.findUnsortedSubarray([2, 1]))
print(s1.findUnsortedSubarray([9, 1, 2, 3, 4, 10]))
print(s1.findUnsortedSubarray([9, 1, 2, 3, 4, 8, 11]))
print(s1.findUnsortedSubarray([1, 3, 2, 4, 5]))
# 4
# 5
# 0
# 4
# 2
# 5
# 6
# 2

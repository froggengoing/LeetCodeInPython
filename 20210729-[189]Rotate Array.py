# Given an array, rotate the array to the right by k steps, where k is non-negat
# ive. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#  [1,2,3,4,5,6,7,8,9]
# 
#  Example 2: 
# 
#  
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 105 
#  -231 <= nums[i] <= 231 - 1 
#  0 <= k <= 105 
#  
# 
#  
#  Follow up: 
# 
#  
#  Try to come up with as many solutions as you can. There are at least three di
# fferent ways to solve this problem. 
#  Could you do it in-place with O(1) extra space? 
#  [123456] 2
#  [561234]
#  Related Topics Array Math Two Pointers 
#  👍 5166 👎 970


# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):
    '''
     相较于前一种，有点取巧的意思,但思路也很新奇
    '''

    def rotate(self, nums, k):
        mid = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, mid - 1)
        self.reverse(nums, mid, len(nums) - 1)

    def reverse(self, nums, start, end):
        index = start
        while index <= (start + end) / 2:
            tmp = nums[index]
            nums[index] = nums[end + start - index]
            nums[end + start - index] = tmp
            index += 1

    '''
    秒啊，自己的思路和这个有点类似，但有一点点不通，所以没算出来
    非常有意思的题目，真正让数组闭环在移动位置
    '''

    def rotate2(self, nums, k):
        k = k % len(nums)
        count = 0
        start = 0
        while count < len(nums):
            current = start
            prev = nums[start]
            while True:
                nxt = (current + k) % len(nums)
                temp = nums[nxt]
                nums[nxt] = prev
                prev = temp
                current = nxt
                count += 1
                if start == current:
                    break
            start += 1

    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''
        暴力两个循环
        '''
        size = len(nums)
        for index in range(k):
            tmp = nums[index]
            nums[index] = nums[size - 1]
            for cur in range(index + 1, size):
                sec = nums[cur]
                nums[cur] = tmp
                tmp = sec


# leetcode submit region end(Prohibit modification and deletion)
# s1 = Solution()
# # n1 = [1, 2, 3, 4 , 5, 6, 7]
# n1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# s1.rotate(n1, 3)
# print(n1)

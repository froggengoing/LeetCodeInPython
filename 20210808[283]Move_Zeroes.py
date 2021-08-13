# Given an integer array nums, move all 0's to the end of it while maintaining t
# he relative order of the non-zero elements. 
# 
#  Note that you must do this in-place without making a copy of the array. 
# 
#  
#  Example 1: 
#  Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#  Example 2: 
#  Input: nums = [0]
# Output: [0]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 104 
#  -231 <= nums[i] <= 231 - 1 
#  
# 
#  
# Follow up: Could you minimize the total number of operations done? Related Top
# ics Array Two Pointers 
#  👍 6184 👎 180

# easy
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def moveZeroes(self, nums):
        lindex = 0
        rindex = 1
        while rindex < len(nums):
            if nums[lindex] == 0:
                if nums[rindex] != 0:
                    nums[lindex] = nums[rindex]
                    nums[rindex] = 0
                    lindex += 1
                    rindex += 1
                else:
                    rindex += 1
            # 若 right - lindex >1 ,则中间必然都是0
            # 那么 nums[lindex]一定为0，即走上面的分支
            # 所以 能进入else分支，只能是right - lindex =1
            # 这个分支不用考虑
            # elif lindex < rindex - 1 and nums[rindex] != 0:
            #     lindex += 1
            else:
                rindex += 1
                lindex += 1

    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #	测试用例:[0,1,0,3,12]
        #	测试结果:[12,1,3,0,0]
        #	期望结果:[1,3,12,0,0]
        # 没有保留原来的顺序，错了
        # 双指针
        lindex = 0
        rindex = len(nums) - 1
        while lindex < rindex:
            if nums[lindex] == 0:
                if nums[rindex] != 0:
                    nums[lindex] = nums[rindex]
                    nums[rindex] = 0
                    rindex -= 1
                    lindex += 1
                else:
                    rindex -= 1
            else:
                lindex += 1


# leetcode submit region end(Prohibit modification and deletion)
s1 = Solution()
n1 = [0, 1, 2, 4, 5, 0, 12, 34, 12, 0]
s1.moveZeroes(n1)
print(n1)
n2 = [0, 1, 0, 3, 12, 0, 0, 0, 0, 0, 0, 20]
s1.moveZeroes(n2)
print(n2)
n3 = [0]
s1.moveZeroes(n3)
print(n3)
n3 = [1, 0, 2, 0, 3, 0, 8, 0, 0, 0, 4]
s1.moveZeroes(n3)
print(n3)

# Given an array of integers nums and an integer target, return indices of the t
# wo numbers such that they add up to target.
#
#  You may assume that each input would have exactly one solution, and you may n
# ot use the same element twice.
#
#  You can return the answer in any order.
#
#
#  Example 1:
#
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#
#  Example 2:
#
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
#
#  Example 3:
#
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
#
#  Constraints:
#
#
#  2 <= nums.length <= 104
#  -109 <= nums[i] <= 109
#  -109 <= target <= 109
#  Only one valid answer exists.
#
#
#
# Follow-up: Can you come up with an algorithm that is less than O(n2) time comp
# lexity? Related Topics 数组 哈希表
#  👍 11628 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d1 = dict()
        for index in range(len(nums)):
            remain = target - nums[index]
            if d1.__contains__(remain):
                return [d1[remain], index]
            d1[nums[index]] = index
        return None

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d1 = dict()
        for index, value in enumerate(nums):
            remain = target - value
            # if remain in d1:// 两者写法都可以
            if remain in d1.keys():
                return [d1[remain], index]
            d1[value] = index
        return None


# leetcode submit region end(Prohibit modification and deletion)
s1 = Solution()
print(s1.twoSum2([1, 2, 3, 4], 6))

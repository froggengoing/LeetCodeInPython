class Solution(object):
    #  返回新数组的长度，超出长度部分不用管

    def removeDuplicates(self, nums):
        index = 0
        cur = 0
        while index < len(nums):
            if nums[index] == nums[cur]:
                pass
            else:
                cur += 1
                nums[cur] = nums[index]
            index += 1
        return cur + 1


# leetcode submit region end(Prohibit modification and deletion)


class Solution1():
    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 删除数组会导致，遍历不到后续的元素
        last = None
        index = 0
        while index < len(nums):
            if nums[index] == last:
                del nums[index]
            else:
                last = nums[index]
                index += 1


s1 = Solution()
nums = [0, 0, 0, 1, 1, 2, 3, 4, 5, 6, 6, 6]
l1 = s1.removeDuplicates(nums)
print(nums)
print(l1)

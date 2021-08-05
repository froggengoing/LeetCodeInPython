# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# nums1的长度为m+n
# 必须在num1的基础上修改
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        '''
        nums1的长度为m+n，要将nums2的值直接加入nums1
        所以应该在nums1从后往前加载元素
        '''
        i1 = m - 1
        i2 = n - 1
        while i1 >= 0 or i2 >= 0:
            if i1 < 0:
                nums1[i1 + i2 + 1] = nums2[i2]
                i2 -= 1
            elif i2 < 0:
                break
                # nums1[i1 + i2] = nums1[i1]
                # i1 -= 1
            elif nums1[i1] >= nums2[i2]:
                nums1[i1 + i2 + 1] = nums1[i1]
                i1 -= 1
            else:
                nums1[i1 + i2 + 1] = nums2[i2]
                i2 -= 1

    def merge2(self, nums1, m, nums2, n):
        """
        必须修改数值nums1，而不是返回值
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i1 = 0
        i2 = 0
        arr = [0] * (m + n)
        while i1 < m or i2 < n:
            if i1 >= m:
                arr[i1 + i2] = nums2[i2]
                i2 += 1
            elif i2 >= n:
                arr[i1 + i2] = nums1[i1]
                i1 += 1
            elif nums1[i1] >= nums2[i2]:
                arr[i1 + i2] = nums2[i2]
                i2 += 1
            else:
                arr[i1 + i2] = nums1[i1]
                i1 += 1
        return arr


# leetcode submit region end(Prohibit modification and deletion)
s1 = Solution()
# res=s1.merge([1, 3, 3, 4, 7, 9], 6, [1, 2, 2, 3, 5, 5, 6, 7, 7, 8], 10)
n1 = [1, 2, 3, 0, 0, 0]
# s1.merge(n1, 3, [2, 5, 6], 3)
# n1 = [1, 3, 3, 4, 7, 9] + [0] * 10
# s1.merge(n1, 6, [1, 2, 2, 3, 5, 5, 6, 7, 7, 8], 10)
n1 = [] + [0] * 10
s1.merge(n1, 0, [1, 2, 2, 3, 5, 5, 6, 7, 7, 8], 10)
print(n1)
print(len(n1))
# You are given the head of a linked list with n nodes. 
# 
#  For each node in the list, find the value of the next greater node. That is, 
# for each node, find the value of the first node that is next to it and has a str
# ictly larger value than it. 
# 
#  Return an integer array answer where answer[i] is the value of the next great
# er node of the ith node (1-indexed). If the ith node does not have a next greate
# r node, set answer[i] = 0. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [2,1,5]
# Output: [5,5,0]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [2,7,4,3,5]
# Output: [7,0,5,5,0]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is n. 
#  1 <= n <= 104 
#  1 <= Node.val <= 109 
#  
#  Related Topics Array Linked List Stack Monotonic Stack 
#  👍 1601 👎 82


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def nextLargerNodes(self, head):
        '''
        优化stack同时保存数据和索引
        :param head:
        :return:
        '''
        tmp = head
        stack = []
        res = []
        while tmp:
            res.append(0)
            index = len(res) - 1
            while stack and stack[-1][1].val < tmp.val:
                j, node = stack.pop()
                res[j] = tmp.val
            stack.append((index, tmp))
            tmp = tmp.next
        return res

    def nextLargerNodes2(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        tmp = head
        res = []
        array = []
        stack = []
        i = 0
        while True:
            array.append(tmp.val)
            res.append(0)
            while stack and tmp.val > array[stack[-1]]:
                cur = stack.pop()
                res[cur] = tmp.val
            tmp = tmp.next
            stack.append(i)
            i += 1
            if not tmp:
                break
        return res
        # leetcode submit region end(Prohibit modification and deletion)


def genListNode(arr):
    head = ListNode()
    tmp = head
    for i in range(len(arr)):
        tmp.next = ListNode(val=arr[i])
        tmp = tmp.next
    return head.next


l1 = genListNode([2, 1, 5])
print(Solution().nextLargerNodes(genListNode([2, 1, 5])))
print(Solution().nextLargerNodes(genListNode([2, 7, 4, 3, 5])))
print(Solution().nextLargerNodes(genListNode([2, 7, 4, 3, 5, 8, 2, 9])))

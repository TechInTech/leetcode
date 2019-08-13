#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = [], []
        while l1 or l2:
            if l1:
                num1.append(l1.val)
                l1 = l1.next
            if l2:
                num2.append(l2.val)
                l2 = l2.next
        n1, n2 = len(num1), len(num2)
        numSum = 0
        for i in range(max(n1, n2)):
            forward = 0
            if i >= n2:
                numSum += (num1[i]) * 10**(i)
            elif i >= n1:
                numSum += (num2[i]) * 10**(i)
            else:
                sum_add = num1[i] + num2[i]
                if sum_add >= 10:
                    forward = sum_add // 10
                    sum_add = sum_add % 10
                numSum += sum_add * 10**(i) + forward * 10**(i+1)
        l3 = ListNode(None)
        head = l3
        numSum = str(numSum)
        for i in range(len(numSum)-1, -1, -1):
            head.next = ListNode(int(numSum[i]))
            head = head.next
        return l3.next


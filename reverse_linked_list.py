# -*- coding: utf-8 -*-
"""reverse linked list.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fPkBXMY1Y3bjBHVNds2FBpfDRF9_eEe4
"""

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current is not None:
          next_node = current.next
          current.next = prev

          prev = current
          current = next_node

        return prev

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Create an instance of the Solution class
solution_instance = Solution()

# Reverse the linked list
new_head = solution_instance.reverseList(head)

# Print the reversed linked list: 5 -> 4 -> 3 -> 2 -> 1
while new_head is not None:
    print(new_head.val, end=" -> ")
    new_head = new_head.next
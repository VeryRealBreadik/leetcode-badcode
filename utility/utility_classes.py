from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @staticmethod
    def create_node_list_from_list(nums: List[int]):
        if len(nums) == 0:
            return None
        
        head_node = ListNode()
        current_node = head_node
        for i in range(len(nums)):
            current_node.val = nums[i]
            if i != len(nums) - 1:
                current_node.next = ListNode()
                current_node = current_node.next
        
        return head_node
    
    @staticmethod
    def to_list(head) -> List[int]:
        if head is None:
            return None
        
        nums = []
        current_node = head
        while current_node:
            nums.append(current_node.val)
            current_node = current_node.next
        
        return nums

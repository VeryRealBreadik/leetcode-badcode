# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val: int = 0, next: object = None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode()
        current_node = dummy_head
        carry = 0
        while l1 or l2 or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum = l1_val + l2_val + carry
            carry = sum // 10
            new_node = ListNode(sum % 10)
            current_node.next = new_node
            current_node = current_node.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy_head.next

def main():
    solution = Solution()
    
    # TODO: Make a proper function to easily create linked list from a regular list
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    result = solution.addTwoNumbers(l1, l2)
    while result:
        print(result.val, end=", ")
        result = result.next


if __name__ == "__main__":
    main()

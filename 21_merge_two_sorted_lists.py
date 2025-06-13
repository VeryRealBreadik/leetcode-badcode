from typing import Optional
from utility.utility_classes import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current_node1 = list1
        current_node2 = list2
        dummy_head = ListNode()
        current_node_merged = dummy_head
        
        while current_node1 or current_node2:
            if (current_node1 and not current_node2) or (current_node1 and current_node2 and current_node1.val <= current_node2.val):
                current_node_merged.next = current_node1
                current_node_merged = current_node_merged.next
                current_node1 = current_node1.next
            elif (current_node2 and not current_node1) or (current_node1 and current_node2 and current_node1.val > current_node2.val):
                current_node_merged.next = current_node2
                current_node_merged = current_node_merged.next
                current_node2 = current_node2.next
        
        return dummy_head.next

def main():
    solution = Solution()
    list11 = [1, 2, 4]; list12 = [1, 3, 4]
    list21 = []; list22 = []
    list31 = []; list32 = [0]
    head11 = ListNode.create_node_list_from_list(list11); head12 = ListNode.create_node_list_from_list(list12)
    head21 = ListNode.create_node_list_from_list(list21); head22 = ListNode.create_node_list_from_list(list22)
    head31 = ListNode.create_node_list_from_list(list31); head32 = ListNode.create_node_list_from_list(list32)
    result1 = solution.mergeTwoLists(head11, head12)
    result2 = solution.mergeTwoLists(head21, head22)
    result3 = solution.mergeTwoLists(head31, head32)
    print(f"{list11, list12}: {ListNode.to_list(result1)}")
    print(f"{list21, list22}: {ListNode.to_list(result2)}")
    print(f"{list31, list32}: {ListNode.to_list(result3)}")


if __name__ == "__main__":
    main()

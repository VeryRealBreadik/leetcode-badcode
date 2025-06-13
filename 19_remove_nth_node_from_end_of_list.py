from typing import Optional
from utility.utility_classes import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        current_node = head
        while current_node:
            nodes.append(current_node)
            current_node = current_node.next
        
        if len(nodes) == 1:
            # return None # Return statement for leetcode
            return ListNode(None) # Actual return statement
        
        if len(nodes) - n == 0:
            head = head.next
        else:
            previous_node = nodes[len(nodes) - n - 1]
            previous_node.next = previous_node.next.next
        
        return head

def main():
    solution = Solution()
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1]
    nums3 = [1, 2]
    head1 = ListNode.create_node_list_from_list(nums1)
    head2 = ListNode.create_node_list_from_list(nums2)
    head3 = ListNode.create_node_list_from_list(nums3)
    n1 = 2
    n2 = 1
    n3 = 2
    result1 = solution.removeNthFromEnd(head1, n1)
    result2 = solution.removeNthFromEnd(head2, n2)
    result3 = solution.removeNthFromEnd(head3, n3)
    print(f"{nums1, n1}: {ListNode.to_list(result1)}")
    print(f"{nums2, n2}: {ListNode.to_list(result2)}")
    print(f"{nums3, n3}: {ListNode.to_list(result3)}")


if __name__ == "__main__":
    main()

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        current = head
        i = 1

        while current.next:
            i += 1
            current = current.next

        step = i - k % i

        if step == 0:
            return head

        current.next = head
        current = head

        for i in range(step - 1):
            current = current.next

        new_head = current.next
        current.next = None

        return new_head
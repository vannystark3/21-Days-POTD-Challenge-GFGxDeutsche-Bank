class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        if head is None:
            return -1
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.data

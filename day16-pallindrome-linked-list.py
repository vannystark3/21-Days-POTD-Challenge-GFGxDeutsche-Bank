class Solution:
    def isPalindrome(self, head):
        #code here
        if not head or not head.next:
            return True
 
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        current = slow
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        first_half = head
        second_half = prev
        
        while second_half: 
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        return True

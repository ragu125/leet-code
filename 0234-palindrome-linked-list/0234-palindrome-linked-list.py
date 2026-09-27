class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        arr=[]

        while head:
            arr.append(head.val)
            head=head.next

        return arr==arr[::-1]    
        
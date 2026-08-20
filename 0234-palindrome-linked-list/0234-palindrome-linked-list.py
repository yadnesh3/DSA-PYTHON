class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []

        current = head

        while current:
            values.append(current.val)
            current = current.next

        return values == values[::-1]
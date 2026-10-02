

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
        prev = None
        currNode = head

        while currNode:
            tempNode = currNode.next
            currNode.next = prev
            prev = currNode
            currNode = tempNode
    
        return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            n = len(lists)
            
            nlists = []
            if n & 1:
                n -= 1
                nlists.append(lists.pop())
                
            for i in range(0, n, 2):
                lcurr, rcurr = lists[i], lists[i + 1]
                dummy = curr = ListNode()
                while lcurr and rcurr:
                    if lcurr.val < rcurr.val:
                        curr.next = lcurr
                        lcurr = lcurr.next
                    else:
                        curr.next = rcurr
                        rcurr = rcurr.next
                    curr = curr.next
                curr.next = lcurr if lcurr else rcurr
                nlists.append(dummy.next)
            
            lists = nlists
        return lists[0] if lists else None
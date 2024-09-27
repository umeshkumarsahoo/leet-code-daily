class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = dummy = ListNode(next=head)
        for _ in range(left-1):
            cur = cur.next
        prev_end = cur
        cur = cur.next
        res = None
        for _ in range(left, right+1):
            nxt, cur.next = cur.next, res
            cur, res = nxt, cur
        prev_end.next.next = cur
        prev_end.next = res
        return dummy.next
        

        

        
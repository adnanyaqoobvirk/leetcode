/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode ghead = new ListNode(0);
        ListNode gcurr = ghead;
        
        ListNode lhead = new ListNode(0);
        ListNode lcurr = lhead;
        
        ListNode curr = head;
        while(curr != null){
            ListNode ncurr = curr.next;
            curr.next = null;
            
            if(curr.val < x){
                lcurr.next = curr;
                lcurr = lcurr.next;
            } else {
                gcurr.next = curr;
                gcurr = gcurr.next;
            }
            
            curr = ncurr;
        }
        
        lcurr.next = ghead.next;
        
        return lhead.next;
    }
}
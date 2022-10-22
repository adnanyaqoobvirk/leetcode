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
    private ListNode nhead;
    
    public ListNode reverseList(ListNode head) {
        if(head == null){
            return head;
        }
        
        this.nhead = null;
        this.helper(head);
        return this.nhead;
    }
    
    private ListNode helper(ListNode curr){
        if(curr.next == null){
            this.nhead = curr;
            return curr;
        }
        
        this.helper(curr.next).next = curr;
        curr.next = null;
        return curr;
    }
}
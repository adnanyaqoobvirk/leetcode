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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if(head == null || head.next == null || left == right){
            return head;
        }
        
        ListNode sentinal = new ListNode(0, head);
        
        ListNode tail = sentinal;
        for(int i = 1; i < left; i++){
            tail = tail.next;
        }
        
        ListNode prev = tail.next, curr = tail.next.next;
        for(int i = 0; i < right - left; i++){
            ListNode ncurr = curr.next;
            curr.next = prev;
            prev = curr;
            curr = ncurr;
        }
        tail.next.next = curr;
        tail.next = prev;
        
        return sentinal.next;
    }
}
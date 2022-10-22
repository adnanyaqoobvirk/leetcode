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
    public ListNode middleNode(ListNode head) {
        ListNode curr = head;
        int size = 0;
        while(curr != null){
            curr = curr.next;
            size++;
        }
        
        curr = head;
        int mid = size / 2;
        for(int i = 0; i < mid; i++){
            curr = curr.next;
        }
        
        return curr;
    }
}
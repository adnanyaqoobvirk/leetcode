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
    public ListNode mergeNodes(ListNode head) {
        ListNode zero = head, curr = head;
        int curr_sum = 0;
        while(curr != null){
            if(curr.val == 0){
                zero.val = curr_sum;
                curr_sum = 0;
                zero.next = curr.next;
                zero = zero.next;
            } else {
                curr_sum += curr.val;
            }
            curr = curr.next;
        }
        return head.next;
    }
}
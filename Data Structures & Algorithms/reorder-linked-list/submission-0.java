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
    public void reorderList(ListNode head) {

        // first i need to reverse the linked lIntStream
        // then after just loop through using one list vs the otherecord

        ListNode reverse = new ListNode(0);

        // so what i need to do is 
        // reverse the last half of the linked list or what i could do isealed
        // is reverse the entire list then just maintain a count

        ListNode slow = head;
        ListNode fast = head;
        while (fast.next != null && fast.next.next != null){

            fast = fast.next.next;
            slow = slow.next;

        }

        ListNode secondHalf = slow.next;
        slow.next = null;
        ListNode current = secondHalf; 
        ListNode prev = null;


        while (current != null){
            ListNode next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }

        ListNode finalList = head;

        while(prev != null){
            ListNode temp = head.next;
            ListNode prevTemp = prev.next;   
            head.next = prev;             
            prev.next = temp;             
            head = temp;                  
            prev = prevTemp;  
        }

    }
}

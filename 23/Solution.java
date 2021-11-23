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
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) {
            return null;
        }
        
        ListNode res = new ListNode();
        ListNode cur = res;
        while (true) {
            boolean flag = true;
            int idx = -1;
            int minNum = 0;
            for (int i = 0; i < lists.length; i++) {
                if (lists[i] != null) {
                    if (idx == -1 || lists[i].val < minNum) {
                        idx = i;
                        minNum = lists[i].val;
                    }
                    flag = false;
                }
            }
            if (flag) {
                break;
            }
            lists[idx] = lists[idx].next;
            cur.next = new ListNode(minNum);
            cur = cur.next;
        }
        
        return res.next;
    }
}
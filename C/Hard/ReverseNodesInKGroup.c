/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode *reverseKGroup(struct ListNode *head, int k)
{
    if (head == NULL || k == 1)
    {
        return head;
    }

    struct ListNode dummy;
    dummy.next = head;

    struct ListNode *groupPrev = &dummy;

    while (1)
    {
        // Find the kth node
        struct ListNode *kth = groupPrev;

        for (int i = 0; i < k; i++)
        {
            kth = kth->next;

            if (kth == NULL)
            {
                return dummy.next;
            }
        }

        struct ListNode *groupNext = kth->next;

        // Reverse the k nodes
        struct ListNode *prev = groupNext;
        struct ListNode *current = groupPrev->next;

        while (current != groupNext)
        {
            struct ListNode *next = current->next;

            current->next = prev;
            prev = current;
            current = next;
        }

        // Connect previous part to reversed group
        struct ListNode *oldStart = groupPrev->next;
        groupPrev->next = kth;

        // Move groupPrev to the end of reversed group
        groupPrev = oldStart;
    }

    return dummy.next;
}
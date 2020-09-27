# Problem
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
  
You may assume the two numbers do not contain any leading zero, except the number 0 itself.  
  
Example:  
  
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)  
Output: 7 -> 0 -> 8  
Explanation: 342 + 465 = 807.  

# Solution
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

namespace AddTwoNumbers
{
    struct ListNode
    {
        int val;
        ListNode* next;
        ListNode() : val( 0 ), next( nullptr ) {}
        ListNode( int x ) : val( x ), next( nullptr ) {}
        ListNode( int x, ListNode* next ) : val( x ), next( next ) {}
    };

    int scanSize( ListNode* l )
    {
        int s = 0;
        auto t = l;
        while ( t )
        {
            s++;
            if ( t->next )
                t = t->next;
            else
                break;
        }
        return s;
    }

    ListNode* addTwoNumbers( ListNode* l1, ListNode* l2 ) {

        ListNode* ret = nullptr;
        ListNode* last_item = nullptr;
        ListNode* traverse = l1;
        ListNode* traverse2 = l2;
        bool has_carry = false;
        bool is_first = true;

        int s1 = scanSize( l1 );
        int s2 = scanSize( l2 );
        int bestSize = s1;

        if ( s2 > s1 )
            bestSize = s2;

        // dummy variable if we run out of nodes
        ListNode* dummy = new ListNode();
        dummy->val = 0;
        dummy->next = nullptr;

        for ( int i = 0; i < bestSize; i++ )
        {
            ListNode* temp = new ListNode();
            int val1 = 0;
            int val2 = 0;

            if ( traverse )
                val1 = traverse->val;
            if ( traverse2 )
                val2 = traverse2->val;

            auto calc = val1 + val2;

            if ( has_carry )
                calc += 1;

            // round off and bring carry
            if ( calc >= 10 ) {
                has_carry = true;
                calc -= 10;
            }
            else
                has_carry = false;

            temp->val = calc;

            if ( is_first ) {
                last_item = temp;
                ret = last_item;
                is_first = false;
            }
            else
            {
                last_item->next = temp;
                last_item = last_item->next;
            }

            if ( traverse2 )
                traverse2 = traverse2->next;
            else
                traverse2 = dummy;

            if ( traverse )
                traverse = traverse->next;
            else
                traverse = dummy;
        }

        // constitute for lack of next item if we have a carry
        if ( has_carry )
        {
            auto temp = new ListNode();
            temp->val = 1;
            last_item->next = temp;
        }

        return ret;
    }
}
```

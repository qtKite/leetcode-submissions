# Problem
21. Merge Two Sorted Lists  
Easy  
  
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.  
  
Example:  
  
Input: 1->2->4, 1->3->4  
Output: 1->1->2->3->4->4  
  
# Solution
  
```c++
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
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        std::vector<int> merged;
        
        ListNode* ret = nullptr;
        ListNode* last = new ListNode();
        
        auto t1 = l1;
        auto t2 = l2;
        
        while(t1)
        {
            merged.push_back(t1->val);     
            if (!t1->next)
                break;      
            t1 = t1->next;
        }
        
        while (t2)
        {
            merged.push_back(t2->val);     
            if (!t2->next)
                break;      
            t2 = t2->next;
        }
        
        if (merged.size() == 0)
            return ret;
        
        std::sort(merged.begin(), merged.end());
    
        ret = last; 
        
        for (int i = 0; i < merged.size();i++)
        {
            if (i==0)
            {
                last->val = merged[i];
            }
            else
            {
                ListNode* temp = new ListNode();
                temp->val = merged[i];
                last->next = temp;
                last = last->next;
            }
        }
        
        return ret;
    }
};
```
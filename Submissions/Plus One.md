# 66. Plus One
Difficulty: Easy  
  
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.  
  
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.  
  
You may assume the integer does not contain any leading zero, except the number 0 itself.  
  
  
Example 1:  
  
Input: digits = [1,2,3]  
Output: [1,2,4]  
Explanation: The array represents the integer 123.  
  
Example 2:  
  
Input: digits = [4,3,2,1]  
Output: [4,3,2,2]  
Explanation: The array represents the integer 4321.  
  
Example 3:  
  
Input: digits = [0]  
Output: [1]  
  
   
  
Constraints:  
  
    1 <= digits.length <= 100  
    0 <= digits[i] <= 9  
  
  
# Solution

```cpp
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        
        // we want to read this backwards and bring any carries to the front
        // if we have a carry at the end, we want to expand the list with an additional 1
        // then return it
        
        // copy the vector
        std::vector<int>ret;
        for (int i:digits)
            ret.push_back(i);
        
        bool carry=false;
        for (int i=digits.size()-1;i>=0;i--)
        {
            if (carry)
                ret[i]++;
            
            if (i==(ret.size()-1))
                ret[i]++;
            
            if (ret[i]>=10) {
                ret[i] -= 10;
                carry=true;
            }
            else
                carry=false;          
        }
        
        if (carry) 
        {
            // we want a new vector with the new element plus everything after
            std::vector<int>ret2;
            ret2.push_back(1);
            for (int i :ret)
                ret2.push_back(i);
            return ret2;
        }
        
        return ret;
    }
};
```

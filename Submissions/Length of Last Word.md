# Problem
58. Length of Last Word
Difficulty: Easy  
  
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.  
  
If the last word does not exist, return 0.  
  
Note: A word is defined as a maximal substring consisting of non-space characters only.  
  
Example:  
  
Input: "Hello World"  
Output: 5  
  
#Solution
  
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) > 0 and not s.isspace():
            a=s.split()
            return len(a[len(a)-1])
        return 0
```
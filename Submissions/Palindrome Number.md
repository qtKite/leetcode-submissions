# Problem
  
Difficulty: Easy  
  
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.  
  
Example 1:  
  
Input: 121  
Output: true  
  
Example 2:  
  
Input: -121  
Output: false  
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.  
  
Example 3:  
  
Input: 10  
Output: false  
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.  
  
Follow up:  
  
Could you solve it without converting the integer to a string?  
  
# Solution
  
```cpp
class Solution {
public:
    int reverse( int x )
	{
		if ( x == INT_MAX || x == INT_MIN ) // will overflow
			return 0;

		int y = x;

		if ( x < 0 ) // remove power, then restore at the end
			y *= -1;

		int ans = 0;
		std::vector<int> a;

		// since this is 32 bit
		// we can have up to 2 billion
		for ( int i = 1000000000; i > 0; i /= 10 )
		{
			int r = y / i;
			if ( r > 0 )
			{
				a.push_back( r );
				y -= r * i;
			}
			else
				a.push_back( 0 );
		}

		int pwr = 1;
		bool ig = true;

		for ( int i : a )
		{
			if ( i != 0 )
				ig = false;

			if ( i == 0 && ig )
				continue;

			// overflow checks
			if ( pwr == 1000000000 && i > 2 )
				return 0;

			if ( ans > 147483647 && i == 2 && pwr == 1000000000 )
				return 0;

			ans += i * pwr;
			if ( pwr != 1000000000 )
				pwr *= 10;
		}

		if ( x < 0 )
			ans *= -1;

		return ans;
	}
    
    bool isPalindrome(int x) {
        if (x<0)
            return false;
        return x == reverse(x);
    }
};
```
# Problem
Difficulty: Easy  
  
Given a 32-bit signed integer, reverse digits of an integer.  
  
Example 1:  
  
Input: 123  
Output: 321  
  
Example 2:  
  
Input: -123  
Output: -321  
  
Example 3:  
  
Input: 120  
Output: 21  
  
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


# Solution 
```cpp
// flips an integer
	// e.g 123 -> 321
	// will also account for integer oveflows and return 0.
	// only supports 32 bit ints
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
```
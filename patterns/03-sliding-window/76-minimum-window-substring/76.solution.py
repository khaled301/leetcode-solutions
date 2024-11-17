'''
Plan is to use dynamic sliding window technique.

There will be two windows (dictionaries), 
one for the target window and another for the current window.

There will be two core comparisons with O(1) time complexity,

First: 
The first comparison is to check if the total characters are equal in both windows,
and we will use "have" and "need" variable for that.
The "have" var will be the number(including frequency) of valid characters in the current window,
and the "need" var will be the number(including frequency) of characters in the target window.

Second:
The second comparison is to check if the frequency of a valid character from the current window,
matches the frequency of that character in the target window.
if they match, then we will increment the "have" variable by 1. 

First we will need to make sure the target window is not empty.
Then we need to know how many unique characters are in the target window,
and map each character to its frequency.

Now if have == need, then we will check if the current substring(compared using the current window)
is the smallest substring compared to the result substring.
We also need to shrink the current window, by moving the left pointer to the right,
and decrementing the value of the character in the current window which 
ultimately reduces the "have" variable by 1.

Note that,
1) if the character in the current window is not in the target window, then we don't care about it.

2) if the character in the current window is in the target window, and frequency matches
only then we need to increment the "have" variable by 1. So "have" value will only be incremented
when the character frequencies are exactly the same.

3) After popping or shrinking the current window from the left, 
if the frequency is less, then we need to decrement the "have" variable by 1.

In short, we are shrinking window from the left while we are expanding window from the right.

'''
class Solution:
        def minWindow(self, s: str, t: str) -> str:
                #  If there is no such substring, return the empty string "" for the edge case.
                if t == "": return ""
                
                # initialize the target and current windows
                countT, window = {}, {}
                
                # initialize the target window
                for c in t:
                        # in this case, use get instead of countT[c] 
                        # Because the countT[c] may not be in the window countT, then set default to 0 and add 1
                        countT[c] = 1 + countT.get(c,0)
                        
                # initialize the variable have and need
                # length of countT gives the length of unique characters in t
                have, need = 0 , len(countT)
                                
                # r is the right pointer and l is the left pointer
                l = 0
                
                # res will be like [left-pointer, right-pointer], so initially set it to [-1,-1]
                # resLen will be initially set to infinity as we are looking for the smallest window
                res, resLen = [-1,-1], float("infinity")
                
                for r in range(len(s)):
                        # get the current character using r pointer
                        c = s[r]
                        
                        #update the current window with the current char
                        window[c] = 1 + window.get(c,0)
                        
                        # check if the current character is in the target window
                        # we don't care about the character that is not in the target window
                        # window[c] == countT[c] means that we satisfy 
                        # the condition of equal characters in both windows
                        if c in countT and window[c] == countT[c]:
                                have += 1
                        
                        # when condition will be met
                        while have == need:
                                # update the result
                                if (r - l + 1) < resLen:
                                        # window
                                        res = [l,r]
                                        
                                        # size of the window
                                        resLen = r - l + 1
                                        
                                # we need to pop from the left of the window by decrementing the left pointer
                                window[s[l]] -= 1
                                
                                # check if the current character is in the target window
                                # and window count is less than countT for that character in s[l]
                                # if so, then decrement the "have" count and increment the left pointer
                                if s[l] in countT and window[s[l]] < countT[s[l]]:
                                        have -= 1
                                        
                                # shift the left pointer as we are looking for the smallest window 
                                l += 1
                
                # return the result
                l, r = res
                return "" if resLen == float("infinity") else s[l:r+1]
                        
                        
                        
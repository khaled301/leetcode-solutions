from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n, l, maxLen, charSet = len(s), 0 , 0, set()
        
        for r in range(n):
            c = s[r]
            if c not in charSet:
                charSet.add(c)
                maxLen = max(maxLen, (r - l + 1))
            else:
                while c in charSet:
                    charSet.remove(s[l])
                    l += 1
                charSet.add(c)
                
        return maxLen

    def newLengthOfLongestSubstring(self, s: str) -> int:
        l, maxLen, charSet = 0 , 0, set()
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxLen = max(maxLen, (r - l + 1))

        return maxLen
            
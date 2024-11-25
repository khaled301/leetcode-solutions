from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # to hold the next greater element for each number in nums2
        nextGreaterNumber = {}
        stack = []
        
        # iterate through nums2
        for xNum in nums2:
            # this monotonic stack technique,
            # ensures to put the value in the stack in decreasing order
            while stack and xNum > stack[-1]:
                # map the next greater number in the dictionary
                nextGreaterNumber[stack.pop()] = xNum
                
            # add the xNum which has no next greater number to the top of the stack
            stack.append(xNum)
            
        # make sure the stack is empty
        while stack:    
            # map the remaining numbers which have no next greater number 
            # from nums2 to the dictionary with the value -1
            nextGreaterNumber[stack.pop()] = -1
            
        # create a new list to map the next greater number for each number in nums1 
        ans = [nextGreaterNumber[num] for num in nums1]
        
        return ans
            
        
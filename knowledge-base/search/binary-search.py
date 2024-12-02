# Binary Search 
# Consider Binary tree as Prefix of False or 
# Suffix of True
# Thats way we can find the boundary
# And That would be by finding either the last True or the first False
#
# arr = [6,7,9, 1, 3]
# here 6, 7, 9 will be True and 1 and 3 will be False
#
# similarly in arr2 = [5 , 3 , 1 ]
# 5 will be True and 3, 1 will be False

class BSearch:
    def __init__(self, arr):
        self.data = arr 
        self.size = len(arr)
        
    def binarySearch(self, target):
        left = 0
        right = self.size - 1 
        
        while left <= right:
            # this is the correct calculation to avoid integer overflow and get the midpoint
            mid = left + (right - left) // 2

            if self.data[mid] == target:
                return mid
            elif self.data[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return -1
    
    def findSquareRoot(self, num):
        if num == 0 or num == 1:
            return num
        
        if num < 0:
            return -1
        
        l, r = 0, num 

        while l <= r:
            # this is the correct calculation to avoid integer overflow and get the midpoint
            m = l + (r - l) // 2
            sqM = m * m
            
            if sqM == num:
                return m
            elif sqM > num:
                r = m - 1
            else:
                l = m + 1

        return -1
    
    def findFirstOccurrence(self, target):
        l, r = 0, self.size - 1 
        res = -1 
        
        while l <= r:
            m = l + (r - l) // 2 

            if self.data[m] >= target:
                res = m 
                r = m - 1
            else: 
                l = m + 1
        
        return res     
    
    def findMaximumElementInRotatedArray(self, nums):
        ans, l, r = -1, 0, len(nums) - 1   
        
        while l < r:
            m = l + (r - l) // 2
            
            if m == 0 or nums[m] > nums[m - 1]:
                ans = m 
                l = m + 1                   
            else:
                r = m
                
        return nums[ans]
    
    # compare the mid with the last element
    def findSmallestElementInRotatedArray(self, nums):
        ans, l, r = -1, 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2 
            
            # Compare with the rightmost element
            if nums[m] > nums[r]:
                # Smallest must be in the right half
                l = m + 1
            else:
                # Smallest is in the left half or at m
                r = m
                
                # we are looking for the first false case
                # target is to find the boundary
                ans = m

        # print(f"ans: {ans}")
        return nums[ans]
        
        
    # compare mid with the first element
    def findSmallestElementInRotatedArrayNotPreferredApproach(self, nums):
        ans, l, r = -1, 0, len(nums) - 1
        
        while l < r:
            m = l + (r - l) // 2
            
            if nums[m] >= nums[0]:
                # Middle is in the first sorted segment; move right
                if nums[m] >= nums[r]:
                    l = m + 1
                else:
                    r = m
                    ans = m
            else:
                # Middle is in the rotated segment; move left
                r = m
                ans = m
        
        return nums[ans]
    
    def findSquareRootWithPrecision(self, num, precision):
        if num == 0 or num == 1:
            return num
        
        if num < 0:
            return -1
        
        l, r, eps = 0, num, 10 ** (-precision) 
        
        print(f"epsilon: {eps}")
        
        while r - l > eps:
            m = l + (r - l) / 2
            print(f"l: {l}, r: {r}, m: {m}")
            
            if m * m < num:
                l = m
            else:
                r = m
                
            print(f"r - l: {r - l}")
                
        return l + (r - l) / 2


if __name__=="__main__":
    arr = [2,3,5,6,8,10,12]
    target = 10
    squareNum = 16
    # squareNum = 20
    # target = 9
    bs = BSearch(arr)
    
    print(bs.binarySearch(target))
    print("-" * 10)
    
    print(bs.findSquareRoot(squareNum))
    print("-" * 10)
    
    print(bs.findFirstOccurrence(4))
    print("-" * 10)
    
    print(bs.findSmallestElementInRotatedArray([6,7,9,15,19,2,3])) # output: 5
    print(bs.findSmallestElementInRotatedArray([24,27,2,15,19,21,23])) # output: 2
    print(bs.findSmallestElementInRotatedArray([6,7,9])) # output: 0
    print("-" * 10)
    
    print(bs.findSmallestElementInRotatedArrayNotPreferredApproach([6,7,9,15,19,2,3])) # output: 5
    print(bs.findSmallestElementInRotatedArrayNotPreferredApproach([24,27,2,15,19,21,23])) # output: 2
    print(bs.findSmallestElementInRotatedArrayNotPreferredApproach([6,7,9])) # output: 0
    print("-" * 10)
        
    print(bs.findMaximumElementInRotatedArray([2,3,4,6,9,12,15,11,8,6,4,1,1,1])) # output: 6
    print(bs.findMaximumElementInRotatedArray([2,3,4,6,9,17,15,11,8,6,4,1,1,1])) # output: 5
    print(bs.findMaximumElementInRotatedArray([2,3,4,6,9,17,19,21,8,6,4,1,1,1])) # output: 7
    print(bs.findMaximumElementInRotatedArray([2,3,4,6,9,1])) # output: 4
    print("-" * 10)
    
    
    print(bs.findSquareRootWithPrecision(2, 4)) # output: 4
    print("-" * 10)
    

from math import *
class Solution:   
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numsLen01 = len(nums1)
        numsLen02 = len(nums2)
        mergedArray = [None] * (numsLen01 + numsLen02)
        mergedArrayLen = len(mergedArray)
        medianIndexArray = []
        i = 0
        j = 0
        k = 0
        if mergedArrayLen < 1: 
            return float(0)
        if mergedArrayLen == 1:
            if numsLen01 == 1:
                return float(nums1[0])
            else:
                return float(nums2[0])
        if mergedArrayLen % 2 == 0:
            medianIndexArray.append(floor(mergedArrayLen/2 - 1))
            medianIndexArray.append(floor(mergedArrayLen/2))
        else:
            medianIndexArray.append(floor(mergedArrayLen/2))
        while i < numsLen01 and j < numsLen02:
            if nums1[i] < nums2[j]:
                mergedArray[k] = nums1[i]
                k += 1
                i += 1
            else:
                mergedArray[k] = nums2[j]
                k += 1
                j += 1
        while i < numsLen01:
                mergedArray[k] = nums1[i]
                k += 1
                i += 1   
        while j < numsLen02:
                mergedArray[k] = nums2[j]
                k += 1
                j += 1
        if len(medianIndexArray) == 1:
            return float(mergedArray[medianIndexArray[0]])
        if len(medianIndexArray) == 2:
            sumOfMiddleValues = mergedArray[medianIndexArray[0]] + mergedArray[medianIndexArray[1]]
            median = float(sumOfMiddleValues/2)
            return median
        return float(0)
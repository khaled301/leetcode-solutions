from typing import List
import heapq

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # store the result
        res = []
        
        # Sort the intervals list based on the start index
        # for eg: [[15, 18], [1,3],[8,10],[2,6]] will become [[1,3],[2,6],[8,10], [15,18]]
        intervals.sort(key=lambda x: x[0])
        
        # loop through the intervals
        for currentInterval in intervals:
            # if the result is empty or the last interval's end is less than the current interval's start
            # add the current interval to the result
            # else update the last interval's end
            # this check ensures that the intervals are non-overlapping
            # first we are checking if the current interval starts before the last interval ends by checking 
            # if it does, that means the current interval overlaps with the last interval
            # so we need to update the last interval's end, 
            # to the max of the current interval's end and the last interval's end to 
            # ensure that the overlapping intervals are merged properly and the end of the merged interval is correct
            # as we are sorting the intervals based on the start index so it is possible to have a scenario where
            # the first interval's end is greater than the second overlapping interval's end, for instance
            # the first interval in the intervals list is [1, 9] and the second interval is [3, 6]
            if not res or res[-1][1] < currentInterval[0]:
                res.append(currentInterval)
            else:
                res[-1][1] = max(res[-1][1], currentInterval[1])
                
        return res
        
from typing import List

class Solution:
    # see the solution for 56 - merge intervals to understand the logic
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            intervals = [newInterval]
            return intervals
        
        # insert the newInterval
        # this is the only difference between the problems, 56 (merge) and 57 (insert) intervals
        intervals.append(newInterval)
        
        intervals.sort(key=lambda x: x[0])
        
        res = []

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res 


    """
        When iterating over the intervals there are three cases:
        1) the new interval's range is before the other
        2) the new interval is after the range of other interval
        3) the new interval is in the range of the other interval
    """
    def insertOptimal(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            intervals = [newInterval]
            return intervals
        
        res = []
        
        for interval in intervals:
            # case 1 | the newInterval is before the range of the interval
            # for eg: new interval = [1, 3] and interval = [4, 5]
            # it helps to maintain the sorted order
            if interval[0] > newInterval[1]:
                res.append(newInterval)
                
                # Set newInterval to the current interval. 
                # This ensures that the current interval is processed as 
                # the next potential interval to insert or merge.
                # eg: update the newInterval to [4, 5]
                newInterval = interval 
                
            # case 2 | the newInterval is after the range of the interval
            # for eg: new interval = [4, 5] and interval = [1, 3]
            elif interval[1] < newInterval[0]:
                res.append(interval)
                
            # case 3 | the newInterval is in the range of the interval
            # for eg: new interval = [3, 4] and interval = [2, 5]
            elif interval[0] <= newInterval[1] or interval[1] >= newInterval[0]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        # After finishing the iteration, append the last newInterval to res. 
        # This ensures that the final merged interval is included in the result and no intervals are omitted.  
        res.append(newInterval)
        
        return res
            
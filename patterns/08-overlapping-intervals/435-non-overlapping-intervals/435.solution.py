from typing import List

class Solution:
    def eraseOverlapIntervalsOptimal(self, intervals: List[List[int]]) -> int:
        # sort intervals (meetings) by end time to know 
        intervals.sort(key=lambda x: x[1])
        
        # total number of meetings
        n = len(intervals)
        
        # store the index of the previous meeting
        # we will use this to check if we can attend the current meeting
        prev = 0
        
        # Insert the first meeting into the schedule
        count = 1

        for i in range(1, n):
            # start of second interval >= end of first interval
            # second meeting starts after the first meeting ends
            # we can attend both meetings | No overlapping
            if intervals[i][0] >= intervals[prev][1]:
                # we can keep the previous meeting
                count += 1
                
                # now we check if we can keep the current one too
                prev = i

        # subtracting the number of meetings we can keep from total meetings
        # gives us the number of meetings we can remove from our schedule
        return n - count
    
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort the intervals
        intervals.sort(key=lambda x: x[0])
        
        # store the non-overlapping intervals
        res = []

        for interval in intervals:
            # if the current interval doesn't overlap with the last interval in res
            # add the current interval to res
            #
            # "<=" because the intervals which only touch at a point are non-overlapping. 
            # For example, [1, 2] and [2, 3] are non-overlapping.
            if not res or res[-1][1] <= interval[0]:
                res.append(interval)
                
            # if the current interval overlaps with the last interval in res
            # make sure it completely overlaps otherwise just ignore the interval
            # update the last interval in res if it completely overlaps with the current interval
            #
            # this required to omit any large overlapping intervals otherwise
            # we will end up removing more intervals than necessary
            # for eg: [[1,100],[11,22],[1,11],[2,12]]
            # here the interval [1, 100] overlaps all other intervals as result
            # we have to remove all other intervals if we keep it which won't be correct
            elif res and (res[-1][0] <= interval[0] and res[-1][1] >= interval[1]):
                res[-1] = interval
        
        # the returned result will be the number of intervals that need to be removed
        # "all intervals" minus "non-overlapping intervals" = number of intervals that need to be removed
        return len(intervals) - len(res)
            
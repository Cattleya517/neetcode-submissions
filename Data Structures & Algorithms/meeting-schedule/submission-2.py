"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)

        for idx, i in enumerate(intervals):
            if idx == 0:
                continue
            if i.start < intervals[idx-1].end:
                return False

        return True
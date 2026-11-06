class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        result = [intervals[0]]

        for idx, i in enumerate(intervals):
            if idx == 0:
                continue
            start, end = i[0], i[1]
            if start > result[-1][1]: #開頭沒有被前一段包住
                result.append(i)
            else:
                result[-1] = [result[-1][0], max(end, result[-1][1])]
        
        return result

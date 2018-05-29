# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:

    def should_merge(self, interval, new_interval):
        cond1 =  (interval[0] <= new_interval[0] <= interval[1]) or (interval[0] <= new_interval[1] <= interval[1])
        cond2 = (new_interval[0] <= interval[0] <= new_interval[1]) or (new_interval[0] <= interval[1] <= new_interval[0])
        return cond1 or cond2

    def merge(self, merge_in, new_interval):
        return [min(merge_in[0], new_interval[0]), max(merge_in[1], new_interval[1])]

    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        
        if not intervals:
            return []

        if not new_interval:
            return intervals


        new_interval = sorted(new_interval)
        start_idx = end_idx = None
        prev_idx = None
        idx = 0
        while True:
            # should merge with previous interval 
            prev_interval = intervals[idx-1]
            current_interval = intervals[idx]
            current_idx = idx
            if prev_idx and self.should_merge(prev_interval, current_interval):
                # should current_interval merge with previous interval
                merged_interval = self.merge(prev_interval, current_interval)
                intervals[idx-1] = merged_interval
                intervals.pop(current_idx)
            elif self.should_merge(current_interval, new_interval):
                # OR should current_interval merge with the new_interval
                merged_interval = self.merge(current_interval, new_interval)
                intervals[idx] = merged_interval
                idx += 1
            elif new_interval[0] > prev_interval[1] and new_interval[1] < current_interval[0]:
                # is it a non overlapping interval between prev_interval and current_interval
                intervals.insert(idx, new_interval)
                idx += 1
            else:
                idx += 1
    
            prev_idx = idx            

            if idx == len(intervals):
                break

        # if list is unchanged, that means, new_interval is not intersecting
        first_interval = intervals[0]
        last_interval = intervals[-1]
    
        if new_interval[1] < first_interval[0]:
            intervals.insert(0, new_interval)
        elif new_interval[0] > last_interval[1]:
            intervals.append(new_interval)
        return intervals

def main():
    soln = Solution()
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    new_interval = [4,9]
    expected = [[1,2], [3,10], [12,16]]
    actual = soln.insert(intervals, new_interval)
    assert actual == expected

    intervals = [[1,2],[3,5],[6,7],[8,10],[13,16]]
    new_interval = [1, 17]
    expected = [[1,17]]
    actual = soln.insert(intervals, new_interval)
    assert actual == expected

    intervals = [[1,2],[3,5],[6,7],[8,10],[13,16]]
    new_interval = [11, 12]
    expected = [[1,2],[3,5],[6,7],[8,10],[11,12],[13,16]]
    actual = soln.insert(intervals, new_interval)
    assert actual == expected

    intervals = [[1,2],[3,5],[6,7],[8,10],[13,16]]
    new_interval = [11, 12]
    expected = [[1,2],[3,5],[6,7],[8,10],[11,12],[13,16]]
    actual = soln.insert(intervals, new_interval)
    assert actual == expected

    intervals = [[1,2],[3,5],[6,7],[8,10],[13,16]]
    new_interval = [-2, 5]
    expected = [[-2, 5],[6,7],[8,10],[13,16]]
    actual = soln.insert(intervals, new_interval)
    assert actual == expected

    intervals = [[1,2],[3,5],[6,7],[8,10],[13,16]]
    new_interval = [-2, 8]
    expected = [[-2,10],[13,16]]
    actual = soln.insert(intervals, new_interval)
    assert actual == expected

    intervals = [[1,2],[3,5],[6,7],[8,10],[13,16]]
    new_interval = [17, 22]
    expected = [[1,2],[3,5],[6,7],[8,10],[13,16], [17,22]]
    actual = soln.insert(intervals, new_interval)
    assert actual == expected

    intervals = [[1,2],[3,5],[6,7],[8,10],[13,16]]
    new_interval = [-5, -2]
    expected = [[-5,-2], [1,2],[3,5],[6,7],[8,10],[13,16]]
    actual = soln.insert(intervals, new_interval)
    assert actual == expected

    intervals = [[1,2],[3,5],[6,7],[8,10],[13,16]]
    new_interval = [-5, 17]
    expected = [[-5,17]]
    actual = soln.insert(intervals, new_interval)
    assert actual == expected

if __name__ == "__main__":
    main()

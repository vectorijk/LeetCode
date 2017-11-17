# Time:  O(nlogn)
# Space: O(n)

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {integer}
    
    #sort
    def minMeetingRooms2(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        time = []
        for interval in intervals:
            time.append((interval.start, 1))
            time.append((interval.end, -1))
        # notice here sort by (x[0], x[1])
        time = sorted(time, key=lambda x: (x[0], x[1]))
        
        cnt = 0
        res = 0
        for t in time:
            cnt += t[1]
            res = max(res, cnt)
        
        return res

    #map
    def minMeetingRooms3(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        time = {}
        for interval in intervals:
            if interval.start not in time:
                time[interval.start] = 1
            else:
                time[interval.start] += 1
                
            if interval.end not in time:
                time[interval.end] = -1
            else:
                time[interval.end] -= 1
        
        rooms, res = 0, 0
        print time
        for t in sorted(time.keys()):
            rooms += time[t]
            res = max(res, rooms)
        
        return res
    
    def minMeetingRooms1(self, intervals):
        starts, ends = [], []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts.sort()
        ends.sort()

        s, e = 0, 0
        min_rooms, cnt_rooms = 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                cnt_rooms += 1  # Acquire a room.
                # Update the min number of rooms.
                min_rooms = max(min_rooms, cnt_rooms)
                s += 1
            else:
                cnt_rooms -= 1  # Release a room.
                e += 1

        return min_rooms
    
    

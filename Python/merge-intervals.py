# Time:  O(nlogn)
# Space: O(1)
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
#

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x.start)
        result = [intervals[0]]
        for i in xrange(1, len(intervals)):
            prev, current = result[-1], intervals[i]
            if current.start <= prev.end: 
                prev.end = max(prev.end, current.end)
            else:
                result.append(current)
        return result
    
#my solution
def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda i: [i.start,i.end])
        
        s = intervals[0].start
        e = intervals[0].end
        result = []
        for i in range(1, len(intervals)):
            if intervals[i].start > e:
                result.append(Interval(s,e))
                s = intervals[i].start
                e = intervals[i].end
            else:
                e = max(e, intervals[i].end)
        result.append(Interval(s,e))
        return result


if __name__ == "__main__":
    print Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15,18)])
    
#merge two sorted list of intervals
# public List<Interval> Intersection(List<Interval> a, List<Interval> b) {
#     var result = new List<Interval>();
#     int i = 0;
#     int j = 0;
#     while(i < a.Count && j < b.Count) {
#         if (a.end <= b[j].start) {
#             i++;
#         }
#         else if(b[j].end <= a.start) {
#             j++;
#         }
#         else {
#             Interval temp = new Interval(Math.Max(a.start, b[j].start), Math.Min(a.end, b[j].end));
#             result.Add(temp);
#             if(a.end <= b[j].end) {
#                 i++;
#             }
#             else {
#                 j++;
#             }
#         }
#     }
#     return result;
# }

    
#merge two sorted list of intervals
# import java.util.*;

# class Interval {
# 	int start;
# 	int end;
# 	public Interval(int start, int end) {
# 		this.start = start;
# 		this.end = end;
# 	}
# }

# class myComparator implements Comparator<Interval> {
# 	@Override
# 	public int compare(Interval i1, Interval i2) {
# 		if (i1.start == i2.start) {
# 			return 0;
# 		} else {
# 			return i1.start < i2.start? -1: 1;
# 		}
# 	}
# }

# public class IntervalMerge {
# 	public List<Interval> mergeList(List<Interval> l1, List<Interval> l2) {
# 		if (l1 == null || l1.size()  == 0) {
# 			return l2;
# 		} else if (l2 == null || l2.size() == 0) {
# 			return l1;
# 		} 
		
# 		Collections.sort(l1, new myComparator());
# 		Collections.sort(l2, new myComparator());
		
# 		List<Interval> result = new ArrayList<>();
# 		int ix1 = 0;
# 		int ix2 = 0;
# 		// Get the first interval
# 		Interval prev = null;
# 		if (l1.get(0).start < l2.get(0).start) {
# 			prev = l1.get(0);
# 			ix1 ++;
# 		} else {
# 			prev = l2.get(0);
# 			ix2 ++;
# 		}
# 		// Move two pointers to merge lists
# 		while (ix1 < l1.size() || ix2 < l2.size()) {
# 			if (ix2 == l2.size() || (ix1 < l1.size() && l1.get(ix1).start < l2.get(ix2).start)) {
# 				// merge prev with ix1
# 				if (prev.end < l1.get(ix1).start) {
# 					result.add(prev);
# 					prev = l1.get(ix1);
# 				} else {
# 					prev.end = Math.max(prev.end, l1.get(ix1).end);
# 				}
# 				ix1 ++;
# 			} else {
# 				// merge prev with ix2
# 				if (prev.end < l2.get(ix2).start) {
# 					result.add(prev);
# 					prev = l2.get(ix2);
# 				} else {
# 					prev.end = Math.max(prev.end, l2.get(ix2).end);
# 				}
# 				ix2 ++;
# 			}
# 		}		
# 		result.add(prev);
# 		return result;
# 	}

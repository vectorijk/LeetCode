import heapq

class point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        return self.x**2 + self.y**2 > other.x**2 + other.y**2
    def __eq__(self, other):
        return self.x**2 + self.y**2 == other.x**2 + other.y**2
    def __str__(self):
        return '('+str(self.x)+', '+str(self.y)+')'

max_heap = []

k = 4

points = [point(1,2), point(4,5), point(7,8), point(2,3), point(3,2),
point(3,4)]

print points[0], points[1]
print points[0] < points[1]

for p in points:
    heapq.heappush(max_heap, p)
    if len(max_heap) == k + 1:
        print heapq.heappop(max_heap)

result = []
while max_heap:
    result.append(heapq.heappop(max_heap))

print map(str, result)

def first_one(arr, start, end):
	while start <= end:
		mid = (start+end)//2
		if arr[mid] == 0:
			start = mid + 1
		else:
			end = mid - 1
	return start

t = [0,0,0,0,1,1,1]
# print firstOne(t, 0, len(t)-1)

def most_left_one(arr):
	n = len(arr)
	if n == 0:
		return -1
	m = len(arr[0])
	if m == 0:
		return -1

	left_idx = False
	end = first_one(arr[0], 0, m-1)
	if end < m:
		left_idx = end
	else:
		end = m-1

	for i in range(1, n):
		if arr[i][end] == 0:
			continue
		else:
			end = first_one(arr[i], 0, end)
			left_idx = end

	return left_idx

arr = [
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,1,1],
[0,0,0,1,1,1,1],
[0,0,0,0,1,1,1]
]

arr2 = [
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]
]

print most_left_one(arr)

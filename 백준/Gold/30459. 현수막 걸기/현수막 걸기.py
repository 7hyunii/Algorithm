import sys
input = sys.stdin.readline
import bisect

N, M, R = map(int, input().split())
A = list(map(int, input().split())) 
B = list(map(int, input().split())) 
A.sort()
B.sort()

ans = -1
for i in range(N):
    for j in range(i+1, N):
        Width = A[j] - A[i]
        A_Height = 2 * R / Width
        
        idx = bisect.bisect_right(B, A_Height)
        
        if idx > 0:
	        Height = B[idx-1]
	        New = Width * Height * 0.5
	        
	        if New <= R:
	        	ans = max(ans, New)

if ans != -1:
	print(f"{ans:.1f}")
else:
	print(-1)
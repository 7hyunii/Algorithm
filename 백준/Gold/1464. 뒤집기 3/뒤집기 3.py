#뒤집고 + 뒤집고
import sys
input = sys.stdin.readline

S = input().rstrip()

for i in range(1, len(S)):
    if S[i-1] > S[i] and S[0] >= S[i]:
        S = S[:i][::-1] + S[i:]
        #print(S, i)
        S = S[:i+1][::-1] + S[i+1:]
        #print(S, i)

print(S)
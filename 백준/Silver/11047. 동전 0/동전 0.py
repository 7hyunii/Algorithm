n, k=map(int, input().split())
a=[int(input()) for _ in range(n)]
a.sort(reverse=True)
c=0
while k>0:
	for i in a:
		if k>=i:
			c+=k//i
			k%=i
print(c)
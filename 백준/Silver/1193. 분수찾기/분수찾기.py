n = int(input())

line = 1
while n > line:
    n -= line
    line += 1

if line % 2:
	x = line - n + 1
	y = n
else:
	x =  n
	y = line - n + 1

print(x, "/", y, sep="")
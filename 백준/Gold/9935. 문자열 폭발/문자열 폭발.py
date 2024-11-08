import sys
input=sys.stdin.readline
stack = []
string = input().rstrip()
exp = list(input().rstrip())
check = len(exp)

for i in range(len(string)):
    stack.append(string[i])
    #print(stack[-check:])
    if stack[-check:] == exp:
        for _ in range(len(exp)):
            stack.pop()

if stack:
    print(*stack, sep="")
else:   
    print("FRULA")
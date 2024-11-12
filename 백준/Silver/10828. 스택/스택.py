import sys
n=int(sys.stdin.readline())
stack=list()
for i in range(n):
    a=sys.stdin.readline().split()
    if (a[0]=="top"):
        if(len(stack)==0):
            print(-1)
        else:
            print(stack[len(stack)-1])
    elif(a[0]=="pop"):
        if(len(stack)==0):
            print(-1)
        else:
            print(stack.pop())
    elif(a[0]=="size"):
        print(len(stack))
    elif(a[0]=="empty"):
        if(len(stack)==0):
            print(1)
        else:
            print(0)
    else:
        stack.append(a[1])
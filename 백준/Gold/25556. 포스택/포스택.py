import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s1, s2, s3, s4 = 0, 0, 0, 0
s1 = arr[0]
for i in range(1, n):
    if arr[i] < s1:
        if s2 == 0:
            s2 = arr[i]
        else:
            if arr[i] < s2:
                if s3 == 0:
                    s3 = arr[i]
                else:
                    if arr[i] < s3:
                        if s4 == 0:
                            s4 = arr[i]
                        else:
                            if arr[i] < s4:
                                print("NO")
                                #print(s1, s2, s3, s4)
                                quit()
                            else:
                                s4 = arr[i]
                    else:
                        s3 = arr[i]
            else:
                s2 = arr[i]
    else:
        s1 = arr[i]

print("YES")
#print(s1, s2, s3, s4)
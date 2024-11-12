import sys
input = sys.stdin.readline

while 1:
    try:
        n = int(input())
        num = 1
        while 1:
            if num % n == 0:
                print(len(str(num)))
                break
            else:
                num = num*10 + 1
    except:
        quit()
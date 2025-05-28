arr=[int(input()) for _ in range(9)]
arr.sort()
delete=sum(arr)-100
for i in range(9):
    SS=0
    for j in range(i+1, 9):
        if arr[i]+arr[j]==delete:
            d1=arr[i]
            d2=arr[j]
            arr.remove(d1)
            arr.remove(d2)
            SS=1
            break
    if SS==1:
        break
print(*arr, sep="\n")
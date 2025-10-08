import sys
input = sys.stdin.readline

class Node:
    def __init__(self, size, index):
        self.size = size
        self.index = index
        self.prev = None
        self.next = None
        self.isAlive = True

head = Node(0, 0)
tail = Node(0, 0)
head.next, tail.prev = tail, head

n = int(input())
arr = list(map(int, input().split()))
cur = head
for i in range(n):
    new = Node(size=arr[i], index=i+1)
    cur.next, new.prev = new, cur
    cur = new
cur.next, tail.prev = tail, cur

while True:
    if head.next == tail.prev:
        break
    
    alive = []
    cur = head.next
    while cur != tail:
        alive.append(cur)
        cur = cur.next
    
    for now in alive:
        if not now.isAlive:
            continue
        Size = now.size

        left = now.prev
        if left != head and left.size <= Size:
            now.size += left.size
            left.isAlive = False
            left = left.prev
            now.prev = left
            left.next = now

        right = now.next
        if right != tail and right.size <= Size:
            now.size += right.size
            right.isAlive = False
            right = right.next
            now.next = right
            right.prev = now

print(head.next.size)
print(head.next.index)
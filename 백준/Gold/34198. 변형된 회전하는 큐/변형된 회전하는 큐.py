import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data=0, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

head = Node()
tail = Node()
head.next = tail
tail.prev = head

n = int(input())
initial_list = list(map(int, input().split()))
Q = int(input())

address = {}
current = head
for val in initial_list:
    new_node = Node(data=val, prev=current)
    current.next = new_node
    address[val] = new_node
    current = new_node
current.next = tail
tail.prev = current

result = []
for _ in range(Q):
    query = input().strip().split()
    cmd = query[0]

    if cmd == "SF":
        if head.next != tail and head.next.next != tail:
            target = head.next
            head.next = target.next
            target.next.prev = head
            
            last_node = tail.prev
            last_node.next = target
            target.prev = last_node
            target.next = tail
            tail.prev = target
    
    elif cmd == "SL":
        if head.next != tail and head.next.next != tail:
            target = tail.prev
            tail.prev = target.prev
            target.prev.next = tail
            
            first_node = head.next
            first_node.prev = target
            target.next = first_node
            target.prev = head
            head.next = target

    elif cmd == "SM":
        x = int(query[1])
        node_x = address[x]
        
        if node_x == head.next:
            if head.next != tail and head.next.next != tail:
                target = head.next
                head.next = target.next; target.next.prev = head
                last_node = tail.prev
                last_node.next = target; target.prev = last_node
                target.next = tail; tail.prev = target

        elif node_x == tail.prev:
            if head.next != tail and head.next.next != tail:
                target = tail.prev
                tail.prev = target.prev; target.prev.next = tail
                first_node = head.next
                first_node.prev = target; target.next = first_node
                target.prev = head; head.next = target
                
        else:
            head_L = head.next
            tail_L = node_x.prev
            head_R = node_x.next
            tail_R = tail.prev

            head.next = head_R
            head_R.prev = head
            
            tail_R.next = node_x
            node_x.prev = tail_R
            
            node_x.next = head_L
            head_L.prev = node_x
            
            tail_L.next = tail
            tail.prev = tail_L
    
    elif cmd == "PF":
        if head.next != tail:
            target = head.next
            result.append(target.data)
            head.next = target.next
            target.next.prev = head
    
    elif cmd == "PL":
        if head.next != tail:
            target = tail.prev
            result.append(target.data)
            tail.prev = target.prev
            target.prev.next = tail
    
    elif cmd == "PM":
        x = int(query[1])
        target = address[x]
        result.append(target.data)
        target.prev.next = target.next
        target.next.prev = target.prev

print(*result)
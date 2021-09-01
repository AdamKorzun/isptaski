class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def delete_duplicates(head):
        cur = head
        while (cur is not None):
            if (cur.value == cur.next.value):
                if (cur.next.next is not None):
                    cur.next = cur.next.next
                    continue
                else:
                    cur.next = None
            cur = cur.next

head = Node(0)
cur = head
for i in range(10):
    cur.next = Node(i)
    cur = cur.next
    cur.next = Node(i)
    cur = cur.next

cur = head
while True:
    try:
        print(cur.value)
        cur = cur.next
    except AttributeError:
        break

head.delete_duplicates()
print('after deleting')

cur = head
while True:
    try:
        print(cur.value)
        cur = cur.next
    except AttributeError:
        break

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Creating linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(50)


# Insert node at beginning
newNode = Node(5)
newNode.next = head
head = newNode


# Print linked list
temp = head

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")
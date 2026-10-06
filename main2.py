class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Creating linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)


# Insert node at end
newNode = Node(40)

temp = head
while temp.next:
    temp = temp.next

temp.next = newNode


# Print linked list
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")
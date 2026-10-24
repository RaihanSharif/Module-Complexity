class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        self.removed = False


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        node = Node(value)
        node.next = self.head

        # set current head's previous node 
        # to be the new head node
        if self.head is not None:
            self.head.prev = node
        else:
            self.tail = node          
        self.head = node
        # returns the node so it can be removed by the remove method
        return node

ll = LinkedList()
ll.push_head(12)
print(ll.head) # a .Node object at 0x...
print(ll.head.value) # 12 .

# size 5
# Node(12) -> Node(2) -> Node(22) -> Node(43) -> Node(4)
#
#
#


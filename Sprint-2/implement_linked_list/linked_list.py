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
            # if no previous head, make current head also the tail
            self.tail = node             
        self.head = node
        # returns the node so it can be removed by the remove method
        return node

    def pop_tail(self):
        if self.tail is None:
            raise IndexError("Cannot pop from empty list")

        # get current tail
        current_tail = self.tail
        # if currnet tail has a previous, set its next to be None
        # if current tail has a previous, set that to be the new tail
        if current_tail.prev is not None:
            current_tail.prev.next = None
            self.tail = current_tail.prev
        else:
            # if current tail has no previous, it must also be the head
            # if it's deleted, list is empty
            self.head = None
            self.tail = None

        # delink current tail's prev, and set removed to True
        # so that putting it inside of remove won't try to remove something
        # that's not in the list
        current_tail.prev = None
        current_tail.removed = True
        return current_tail



ll = LinkedList()
ll.push_head(2)
ll.push_head(12)

if ll.tail is not None:
    print(ll.tail.value)
else:
    print("list is empty")

ll.pop_tail()

if ll.tail is not None:
    print(ll.tail.value)
else:
    print("list is empty")

ll.pop_tail()

if ll.tail is not None:
    print(ll.tail.value)
else:
    print("list is empty")


# size 5
# Node(12) -> Node(2) -> Node(22) -> Node(43) -> Node(4)
# Node(12) -> Node(2)
# Node(12)   head: Node(12)   tail: Node(12)
#



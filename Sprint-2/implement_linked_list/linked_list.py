class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0
        if self.head is not None:
            self.size += 1
        if self.tail is not None and self.head != self.tail:
            self.size += 1

    def push_head(self, new_head):
        new_head.next = self.head
        self.head = new_head
        self.size += 1
        return self.head

    def pop_tail(self):
        node_before_last = self.head
        for i in range(self.size - 2):
            node_before_last = node_before_last.next
        tail = node_before_last.next
        self.tail = node_before_last
        return tail

# size 5
# Node(12) -> Node(2) -> Node(22) -> Node(43) -> Node(4)
#
#
#


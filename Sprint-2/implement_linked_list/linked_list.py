class Node:
    __slots__ = ("value", "prev", "next", "owner")
    
    def __init__(self, value, owner):
        self.value = value
        self.prev = None
        self.next = None
        # this links a node to a specific list
        # prevents attempt to remove a node from a list
        # it does not belong to.
        self.owner = owner   


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        node = Node(value, self) # makes this list the owner
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

        current_tail = self.tail
        self.remove(current_tail)

        return current_tail.value

    def remove(self, node):
        # check if node is a removed node
        if node.owner is None:
            return

        if node.owner is not self:
            raise ValueError("This node does not belong to this list")
        
        # delink the node
        if node.prev is not None:
            node.prev.next = node.next
        else:
            # removing head
            self.head = node.next

        
        if node.next is not None:
            node.next.prev = node.prev
        else:
            # removing tail
            self.tail = node.prev

        # removed node should not keep refereces into the list
        # otherwise it could leave other nodes alive.
        # could mislead users of the removed node about the state
        # of the list
        node.prev = None 
        node.next = None

        node.owner = None



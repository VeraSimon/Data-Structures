"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        # Is the list empty? Just create a node without prev and next, then set
        # head and tail to the node.
        # If there's something in the list, create a node with the previous
        # head as next, then set the new node as head.
        pass

    def remove_from_head(self):
        # If the list is empty, return None.
        # If head and tail are the same, set them both to None.
        # Otherwise, set head to the second item in the LL, then set the new
        # head's prev value to None, orpahning the original head. Return the
        # original head.
        pass

    def add_to_tail(self, value):
        # Is the list empty? Just create a node without prev and next, then set
        # head and tail to the node.
        # If there's something in the list, create a node with the previous
        # tail as prev, then set tail to the new node.
        pass

    def remove_from_tail(self):
        # If the list is empty, return None.
        # If head and tail are the same, set them both to None.
        # Otherwise, set the second to last node in the list to tail, then set
        # the new tail's next value to None, orphaning the original tail.
        # Return the original tail.
        pass

    def move_to_front(self, node):
        # If node doesn't exist, raise an exception.
        # https://docs.python.org/3/library/exceptions.html#exception-hierarchy
        # If head and tail are the same, return.
        # Otherwise, set node.prev.next to node.next.prev and vice versa. Then
        # set node.next to the current head and node.prev to None. Finally, set
        # the head to the passed in node.
        pass

    def move_to_end(self, node):
        # If node doesn't exist, raise an exception.
        # https://docs.python.org/3/library/exceptions.html#exception-hierarchy
        # If head and tail are the same, do nothing.
        # Otherwise, walk to the node in question, set node.prev.next to
        # node.next.prev and vice versa. Then set node.prev to the current tail
        # and node.next to None. Finally, set the tail to the passed in node.
        pass

    def delete(self, node):
        # If node doesn't exist, raise an exception.
        # https://docs.python.org/3/library/exceptions.html#exception-hierarchy
        # If head and tail are the same, set both to None.
        # Otherwise, set node.prev.next to node.next.prev and vice versa,
        # orpahning the passed node.
        pass

    def get_max(self):
        # If the list is empty, return None.
        # Walk the list, checking if the current value is greater than the
        # previously found high value, updating as necessary. Return value
        # after walking the list.
        pass

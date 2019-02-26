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
        if not self.head:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        # If there's something in the list, create a node with the previous
        # head as next, then set the new node as head.
        else:
            self.head.insert_before(value)
            self.head = self.head.prev

    def remove_from_head(self):
        # If the list is empty, return None.
        if not self.head:
            return None
        # If head and tail are the same, set them both to None and return the
        # node.
        elif self.head == self.tail:
            tmp_node = self.head
            self.head = None
            self.tail = None
            return tmp_node.value
        # Otherwise, set head to the second item in the LL, then set the new
        # head's prev value to None, orpahning the original head. Return the
        # original head.
        else:
            tmp_node = self.head
            self.head = tmp_node.next
            self.head.prev = None
            return tmp_node.value

    def add_to_tail(self, value):
        # Is the list empty? Just create a node without prev and next, then set
        # head and tail to the node.
        if not self.head:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        # If there's something in the list, create a node with the previous
        # tail as prev, then set tail to the new node.
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

    def remove_from_tail(self):
        # If the list is empty, return None.
        if not self.head:
            return None
        # If head and tail are the same, set them both to None.
        elif self.head == self.tail:
            tmp_node = self.head
            self.head = None
            self.tail = None
            return tmp_node.value
        # Otherwise, set the second to last node in the list to tail, then set
        # the new tail's next value to None, orphaning the original tail.
        # Return the original tail.
        else:
            tmp_node = self.tail
            self.tail = tmp_node.prev
            self.tail.next = None
            return tmp_node.value

    def move_to_front(self, node):
        # If node and head are the same, return.
        if node == self.head:
            return
        # Tail case
        elif node == self.tail:
            old_tail = self.tail
            self.tail = old_tail.prev
            self.head.prev = old_tail
            self.head.prev.next = self.head
            self.head = old_tail
        # Otherwise, set node.prev.next to node.next.prev and vice versa. Then
        # set node.next to the current head and node.prev to None. Finally, set
        # the head to the passed in node.
        else:
            node.delete()
            node.next = self.head
            node.prev = None
            self.head = node

    def move_to_end(self, node):
        # If node and tail are the same, return.
        if node == self.tail:
            return
        # Head case
        elif node == self.head:
            old_head = self.head
            self.head = old_head.next
            self.tail.next = old_head
            self.tail.next.prev = self.tail
            self.tail = old_head
        # Otherwise, set node.prev.next to node.next.prev and vice versa. Then
        # set node.prev to the current tail and node.next to None. Finally, set
        # the tail to the passed in node.
        else:
            node.delete()
            node.prev = self.tail
            node.next = None
            self.tail = node

    def delete(self, node):
        # If head and tail are the same, set both to None.
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
        # Head case
        if node == self.head:
            node.delete()
            self.head = node.next
        # Tail case
        elif node == self.tail:
            node.delete()
            self.tail = node.prev
        # Otherwise, set node.prev.next to node.next.prev and vice versa,
        # orpahning the passed node.
        else:
            # node.prev.next, node.next.prev = node.next.prev, node.prev.next
            node.delete()

    def get_max(self):
        # If the list is empty, return None.
        if not self.head:
            return None
        # Walk the list, checking if the current value is greater than the
        # previously found high value, updating as necessary. Return value
        # after walking the list.
        else:
            max = self.head.value
            cur_node = self.head
            while cur_node.next:
                if cur_node.value < cur_node.next.value:
                    max = cur_node.next.value
                cur_node = cur_node.next
            return max

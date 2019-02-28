class Heap:
    def __init__(self):
        self.storage = []

    # `insert` adds the input value into the heap; this method should ensure
    # that the inserted value is in the correct spot in the heap.
    def insert(self, value):
        self.storage.append(value)
        # if self.get_size() > 1:
        #     node_index = self.get_size() - 1
        #     while self.storage[node_index] > self.storage[(node_index - 1) // 2] and (node_index - 1) // 2 >= 0:
        #         node_parent = (node_index - 1) // 2
        #         self.storage[node_index], self.storage[node_parent] = self.storage[node_parent], self.storage[node_index]
        #         node_index = node_parent

    # `delete` removes and returns the 'topmost' value from the heap; this
    # method needs to ensure that the heap property is maintained after the
    # topmost element has been removed.

    def delete(self):
        pass

    # `get_max` returns the maximum value in the heap _in constant time_.
    def get_max(self):
        return self.storage[0]

    # OwO <(What's this?)
    def get_size(self):
        return len(self.storage)

    # `_bubble_up` moves the element at the specified index "up" the heap by
    # swapping it with its parent if the parent's value is less than the value
    # at the specified index.
    def _bubble_up(self, index):
        parent = (index - 1) // 2
        if self.storage[index] > self.storage[parent] and self.storage[parent] >= 0:
            self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
            return parent
        else:
            return index

    # `_sift_down` grabs the indices of this element's children and determines
    # which child has a larger value. If the larger child's value is larger
    # than the parent's value, the child element is swapped with the parent.
    def _sift_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        # TODO: Need case to check if children are either leaf nodes or out of bounds
        if self.storage[index] < self.storage[left_child] and self.storage[index] > self.storage[right_child]:
            self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
            return left_child
        elif self.storage[index] > self.storage[left_child] and self.storage[index] < self.storage[right_child]:
            self.storage[index], self.storage[right_child] = self.storage[right_child], self.storage[index]
            return right_child
        # Could have extended elif #1 with an `or` + elif #2 logic, but that
        # would have just been long and difficult to read.
        elif self.storage[left_child] == self.storage[right_child] and self.storage[index] < self.storage[right_child]:
            self.storage[index], self.storage[right_child] = self.storage[right_child], self.storage[index]
            return right_child
        else:
            return index

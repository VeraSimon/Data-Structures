class Heap:
    def __init__(self):
        self.storage = []

    # `insert` adds the input value into the heap; this method should ensure
    # that the inserted value is in the correct spot in the heap.
    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size() - 1)

    # `delete` removes and returns the 'topmost' value from the heap; this
    # method needs to ensure that the heap property is maintained after the
    # topmost element has been removed.
    def delete(self):
        # if self.get_size() > 2:
        #     self.storage[0], self.storage[self.get_size() - 1] = \
        #         self.storage[self.get_size() - 1], self.storage[0]
        #     deleted = self.storage.pop(self.get_size() - 1)
        #     node_index = 0
        #     while self.storage[node_index] < self.storage[2 * node_index + 1] or \
        #             self.storage[node_index] < self.storage[2 * node_index + 2]:
        #         new_index = self._sift_down(node_index)
        #         if new_index != node_index:
        #             node_index = new_index
        #     return deleted
        # else:
        #     return self.storage.pop(0)
        self.storage[0], self.storage[self.get_size() - 1] = \
            self.storage[self.get_size() - 1], self.storage[0]
        deleted = self.storage.pop()
        self._sift_down(0)
        return deleted

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
        while index > 0:
            parent = (index - 1) // 2
            if self.storage[index] > self.storage[parent] and self.storage[parent] >= 0:
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                index = parent
            else:
                break

    # `_sift_down` grabs the indices of this element's children and determines
    # which child has a larger value. If the larger child's value is larger
    # than the parent's value, the child element is swapped with the parent.
    def _sift_down(self, index):
        # Ternary shenanigans to determine which child value is larger, then
        # saving the index of the larger (or rightmost when equal) one.
        work_child = 2 * index + 1 \
            if 2 * index + 2 < self.get_size() and \
            self.storage[2 * index + 1] > self.storage[2 * index + 2] \
            else 2 * index + 2

        while work_child <= self.get_size() - 1:
            if self.storage[index] < self.storage[work_child]:
                self.storage[index], self.storage[work_child] = self.storage[work_child], self.storage[index]
                index = work_child
                # Ternary again
                work_child = 2 * index + 1 \
                    if 2 * index + 2 < self.get_size() and \
                    self.storage[2 * index + 1] > self.storage[2 * index + 2] \
                    else 2 * index + 2
            else:
                break

class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        # A list or linked list depending how frisky we're feeling. Given the
        # len method in place, a regular list would probably be more concise
        # here, though the existence of self.size could definitely make a
        # linked list work. Given the nature of a singly linked list, they
        # could definitely add further constraint on managing self.storage,
        # along with easing the need for contiguous memory if the list gets
        # especially large.
        # There's also apparently a collections.deque object one can use for
        # this, but I think that kind of defeats the purpose right now, so I'll
        # go about this from a more primative way.
        self.storage = []

    def enqueue(self, item):
        self.storage.append(item)
        self.size = self.len()

    def dequeue(self):
        if self.len() > 0:
            popped = self.storage.pop(0)
            self.size = self.len()
            return popped
        else:
            return None

    def len(self):
        return len(self.storage)

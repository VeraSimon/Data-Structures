Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`? O(1)

2. What is the runtime complexity of `dequeue`? O(k)

3. What is the runtime complexity of `len`? O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`? Worst case is O(n) if the data being added is sorted beforehand, though really, it's O(h), with h being the height of the tree.

2. What is the runtime complexity of `contains`? O(h)

3. What is the runtime complexity of `get_max`? O(h)

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`? O(c)

2. What is the runtime complexity of `ListNode.insert_before`? O(c)

3. What is the runtime complexity of `ListNode.delete`? O(c)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`? O(c)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`? O(c)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`? O(c)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`? O(c)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`? O(c)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`? O(c)

10. What is the runtime complexity of `DoublyLinkedList.delete`? O(c)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    JS Array.splice in O(n) in the worst case. The DLL runtime as implemented here is O(1) since we know the location from the passed node reference. Therefore, DLL.delete wins.

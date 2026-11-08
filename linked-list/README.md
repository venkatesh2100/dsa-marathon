# Linked List

| Problem | Best Approach | Time | Space | Notes |
|---|---|---|---|---|
| [Reverse Linked List](reverse-linked-list/) | In-place three-pointer walk | O(n) | O(1) | Capture `curr.next` *before* flipping the arrow; same node objects relinked — genuinely in-place; recursion costs O(n) stack and can hit Python's ~1000-frame cap on long lists |
| [Merge Two Sorted Lists](merge-two-sorted-lists/) | Dummy-head iterative splice | O(n + m) | O(1) | Dummy guard makes "return the head" free of special cases; `<=` keeps ties stable (list1 leads); the two drain loops collapse to `tail.next = list1 if list1 else list2` since the survivor is pre-sorted |

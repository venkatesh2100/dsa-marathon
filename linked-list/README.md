# Linked List

| Problem | Best Approach | Time | Space | Notes |
|---|---|---|---|---|
| [Reverse Linked List](reverse-linked-list/) | In-place three-pointer walk | O(n) | O(1) | Capture `curr.next` *before* flipping the arrow; same node objects relinked — genuinely in-place; recursion costs O(n) stack and can hit Python's ~1000-frame cap on long lists |

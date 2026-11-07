# Binary Search

| Problem | Best Approach | Time | Space | Notes |
|---|---|---|---|---|
| [Binary Search](binary-search/) | Halve window with `mid ± 1` | O(log n) | O(1) | Pointer must jump past `mid`; ±1 steps degrade to O(n) |
| [Search a 2D Matrix](search-a-2d-matrix/) | Flatten to 1D, `divmod` map | O(log(m·n)) | O(1) | Legal because rows chain into one sorted sequence |

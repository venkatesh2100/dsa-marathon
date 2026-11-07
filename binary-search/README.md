# Binary Search

| Problem | Best Approach | Time | Space | Notes |
|---|---|---|---|---|
| [Binary Search](binary-search/) | Halve window with `mid ± 1` | O(log n) | O(1) | Pointer must jump past `mid`; ±1 steps degrade to O(n) |
| [Search a 2D Matrix](search-a-2d-matrix/) | Flatten to 1D, `divmod` map | O(log(m·n)) | O(1) | Legal because rows chain into one sorted sequence |
| [Koko Eating Bananas](koko-eating-bananas/) | Binary search on the answer | O(n · log m) | O(1) | Lower-bound template: `l < r` + `r = mid` |
| [Find Minimum in Rotated Sorted Array](find-minimum-in-rotated-sorted-array/) | Binary search, compare mid vs right end | O(log n) | O(1) | Lower-bound template again; compare to `r`, not `l` — left comparison can't tell sorted from rotated |
| [Search in Rotated Sorted Array](search-in-rotated-sorted-array/) | One-pass: sorted half's range vetoes the other | O(log n) | O(1) | Template A; half-detection must use `<=` (mid==l on tiny windows), range checks are half-open |

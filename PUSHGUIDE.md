# Push Guide — DSA Marathon

How every problem gets added: one folder, three files, one push.

## 1. Folder Layout

```
<topic>/
└── <problem-name>/
    ├── my_solution.py        # my original attempt, unchanged
    ├── optimal_solution.py   # best approach, interview-ready
    └── notes.md              # complexity, tradeoffs, which to pick
```

**Naming:** lowercase, hyphenated.

```
arrays/contains-duplicate
arrays/two-sum
sliding-window/longest-substring-without-duplicates
```

## 2. What Goes in Each File

### `my_solution.py`

- My pasted code, kept as-is.
- Add imports only if missing (e.g. `from typing import List`).
- Must run without edits.

### `optimal_solution.py`

- The cleanest optimal solution.
- Only the imports it needs.
- Comments only where the logic is non-obvious.

### `notes.md` — template

```markdown
# <Problem Name>

**Problem:** One-sentence restatement.

**Links:** [NeetCode](...) · [LeetCode](...)

---

## My Solution — <approach name>

Short explanation of the idea.

| | |
|---|---|
| **Time** | O(?) |
| **Space** | O(?) |

**Caveat:** Any worst-case or practical caveat.

## Optimal Solution — <approach name>

Short explanation of why it is optimal.

| | |
|---|---|
| **Time** | O(?) |
| **Space** | O(?) |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Hash set | **O(n)** | O(n) | Default answer |
| Sorting | O(n log n) | O(1) | Memory is tight, input may be mutated |
| Brute force | O(n²) | O(1) | Never — only for comparison |

**Interview answer:** One or two sentences on what to say and code.

## Edge Cases

- Empty input →
- Single element →
- All distinct →
- Duplicates at the start / end →
```

## 3. Update the Indexes

Add the problem to both tables:

- `README.md` — progress table at the root
- `<topic>/README.md` — topic table (e.g. `arrays/README.md`)

Format:

```markdown
| arrays | [Two Sum](arrays/two-sum/) | O(n) | O(n) | ✅ |
```

## 4. Test Before Pushing

```bash
python3 - <<'PY'
import sys
sys.path.insert(0, "arrays/<problem-name>")
from my_solution import Solution as Mine
from optimal_solution import Solution as Optimal

cases = [([], None), ([1], None)]  # (input, expected)
for nums, expected in cases:
    assert Mine().solve(nums) == expected
    assert Optimal().solve(nums) == expected
print("All tests passed")
PY
```

## 5. Commit and Push

```bash
cd ~/dsa-marathon

git add .
git commit -m "Add <topic>/<problem-name>"
git push
```

First push of a brand-new repo:

```bash
git init -b main
git add .
git commit -m "Initial commit"
gh repo create dsa-marathon --public --source=. --remote=origin --push
```

## 6. Paste-Ready Prompt

Copy this into the chat every time I solve a new problem:

````text
Add this to dsa-marathon.

Problem: <problem name>
Topic: <arrays / two-pointers / sliding-window / ...>
Link: <neetcode or leetcode url>

My solution:
```python
<paste code here>
```

Do the usual:
1. Save my code unchanged as my_solution.py (add missing imports).
2. Write the optimal solution as optimal_solution.py.
3. Write notes.md: time/space for both, tradeoffs, which to pick, edge cases.
4. Update README.md and <topic>/README.md tables.
5. Test both solutions against edge cases.
6. Commit and push with message "Add <topic>/<problem-name>".
````

## 7. Checklist

- [ ] Folder is `<topic>/<problem-name>/`
- [ ] `my_solution.py` runs unchanged
- [ ] `optimal_solution.py` is the best approach
- [ ] `notes.md` has both complexities + which to pick
- [ ] Root and topic `README.md` updated
- [ ] Both solutions tested
- [ ] `git add . && git commit && git push`

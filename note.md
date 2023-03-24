# Use of Diction


```python
    # Count frequency of each element in nums1
    freq = {}
    res = []
    for num in nums1:
        freq[num] = freq.get(num, 0) + 1
```

将数字列表转化成字典



# [`itertools`](https://docs.python.org/2/library/itertools.html#module-itertools) — Functions creating iterators for efficient looping

itertools.permutations(*iterable*[, *r*])
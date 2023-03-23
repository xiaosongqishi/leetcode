# 字典的使用
        

```python
    # Count frequency of each element in nums1
    freq = {}
    res = []
    for num in nums1:
        freq[num] = freq.get(num, 0) + 1
```

将数字列表转化成字典
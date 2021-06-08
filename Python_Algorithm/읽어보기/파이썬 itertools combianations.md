# 파이썬 itertools combianations

```python
0 0 0 0 0
0 1 0 0 0 
1 0 1 1 0 
0 0 1 0 0
0 0 0 0 1
```

여러개의 1이 있다 >> 1의 좌표 6개 있는데

3군데만 남기고 싶어.

list(combinations(좌표담은리스트, 3))

일케 하면 됨. 그러면 모든 경우에 대해 나옴
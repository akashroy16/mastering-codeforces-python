n = int(input())
a = list(map(int, input().split()))
 
max_val = max(a)
min_val = min(a)
 
max_idx = a.index(max_val)
min_idx = len(a) - 1 - a[::-1].index(min_val)
 
moves = max_idx + (n - 1 - min_idx)
 
if max_idx > min_idx:
    moves -= 1
 
print(moves)

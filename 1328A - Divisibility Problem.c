import sys
 
input = sys.stdin.read
data = input().split()
 
t = int(data[0])
results = []
 
idx = 1
for _ in range(t):
    a = int(data[idx])
    b = int(data[idx + 1])
    idx += 2
    
    if a % b == 0:
        results.append(0)
    else:
        results.append(b - (a % b))
 
print('\n'.join(map(str, results)))

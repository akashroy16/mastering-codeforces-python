import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1:n+1]]
    
    total_ones = sum(a)
    if total_ones == n:
        print(n - 1)
        return
        
    max_gain = 0
    curr_gain = 0
    for x in a:
        val = 1 if x == 0 else -1
        curr_gain += val
        if curr_gain < 0:
            curr_gain = 0
        if curr_gain > max_gain:
            max_gain = curr_gain
            
    print(total_ones + max_gain)

if __name__ == '__main__':
    solve()

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    h = [int(x) for x in data[2:2+n]]
    
    curr_sum = sum(h[:k])
    min_sum = curr_sum
    best_idx = 1
    
    for i in range(1, n - k + 1):
        curr_sum = curr_sum - h[i - 1] + h[i + k - 1]
        if curr_sum < min_sum:
            min_sum = curr_sum
            best_idx = i + 1
            
    print(best_idx)

if __name__ == '__main__':
    solve()

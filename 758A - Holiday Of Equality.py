import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    a = [int(x) for x in data[1:1+n]]
    
    max_val = max(a)
    total_needed = sum(max_val - x for x in a)
    print(total_needed)

if __name__ == '__main__':
    solve()

import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    ops = 0
    while m > n:
        if m % 2 == 0:
            m //= 2
        else:
            m += 1
        ops += 1
        
    ops += (n - m)
    print(ops)

if __name__ == '__main__':
    solve()

import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n, m, a, b = map(int, data)
    
    cost1 = n * a
    cost2 = (n // m) * b + (n % m) * a
    cost3 = ((n + m - 1) // m) * b
    
    print(min(cost1, cost2, cost3))

if __name__ == '__main__':
    solve()

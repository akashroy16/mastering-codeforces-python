import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    
    max_teams = (n - m + 1) * (n - m) // 2
    
    base = n // m
    rem = n % m
    min_teams = rem * (base + 1) * base // 2 + (m - rem) * base * (base - 1) // 2
    
    print(f"{min_teams} {max_teams}")

if __name__ == '__main__':
    solve()

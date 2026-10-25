import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1:n+1]]
    
    total = sum(a)
    if total % 3 != 0 or n < 3:
        print(0)
        return
        
    target = total // 3
    s = 0
    count = 0
    ways = 0
    
    # First pass to count valid prefix sums
    pref_counts = [0] * n
    for i in range(n - 1, -1, -1):
        s += a[i]
        if s == target:
            count += 1
        pref_counts[i] = count
        
    s = 0
    for i in range(n - 2):
        s += a[i]
        if s == target:
            ways += pref_counts[i + 2]
    print(ways)

if __name__ == '__main__':
    solve()

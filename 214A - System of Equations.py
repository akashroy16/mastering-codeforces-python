import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    
    count = 0
    for a in range(1000):
        for b in range(1000):
            if a * a + b == n and a + b * b == m:
                count += 1
    print(count)

if __name__ == '__main__':
    solve()

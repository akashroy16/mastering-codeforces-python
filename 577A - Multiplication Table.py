import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    x = int(data[1])
    
    count = 0
    for i in range(1, n + 1):
        if x % i == 0 and x // i <= n:
            count += 1
    print(count)

if __name__ == '__main__':
    solve()

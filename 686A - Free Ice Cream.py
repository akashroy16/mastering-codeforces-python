import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    x = int(data[1])
    
    idx = 2
    distressed = 0
    for _ in range(n):
        sign = data[idx]
        d = int(data[idx+1])
        idx += 2
        if sign == '+':
            x += d
        else:
            if x >= d:
                x -= d
            else:
                distressed += 1
    print(f"{x} {distressed}")

if __name__ == '__main__':
    solve()

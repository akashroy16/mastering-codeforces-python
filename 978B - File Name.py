import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    s = data[1]
    
    ans = 0
    count = 0
    for ch in s:
        if ch == 'x':
            count += 1
            if count >= 3:
                ans += 1
        else:
            count = 0
    print(ans)

if __name__ == '__main__':
    solve()

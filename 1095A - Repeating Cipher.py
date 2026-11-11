import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    s = data[1]
    res = []
    curr = 0
    step = 1
    while curr < n:
        res.append(s[curr])
        curr += step
        step += 1
    print("".join(res))

if __name__ == '__main__':
    solve()

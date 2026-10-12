import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        mins = []
        seconds = []
        for _ in range(n):
            m = int(data[idx])
            arr = sorted([int(x) for x in data[idx+1:idx+1+m]])
            idx += 1 + m
            mins.append(arr[0])
            seconds.append(arr[1])
        min_overall = min(mins)
        ans = min_overall + sum(seconds) - min(seconds)
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()

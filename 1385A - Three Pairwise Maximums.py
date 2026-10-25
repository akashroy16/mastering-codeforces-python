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
        arr = sorted([int(data[idx]), int(data[idx+1]), int(data[idx+2])])
        idx += 3
        if arr[1] == arr[2]:
            out.append("YES")
            out.append(f"{arr[0]} {arr[0]} {arr[2]}")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()

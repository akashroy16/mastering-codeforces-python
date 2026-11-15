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
        s = data[idx + 1].lower()
        idx += 2
        dedup = []
        for char in s:
            if not dedup or dedup[-1] != char:
                dedup.append(char)
        if "".join(dedup) == "meow":
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()

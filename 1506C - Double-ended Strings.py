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
        a = data[idx]
        b = data[idx+1]
        idx += 2
        
        max_len = 0
        for i in range(len(a)):
            for j in range(i + 1, len(a) + 1):
                sub = a[i:j]
                if sub in b:
                    max_len = max(max_len, len(sub))
        out.append(str(len(a) + len(b) - 2 * max_len))
    print("\n".join(out))

if __name__ == '__main__':
    solve()

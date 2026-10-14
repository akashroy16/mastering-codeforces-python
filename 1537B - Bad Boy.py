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
        m = int(data[idx+1])
        i = int(data[idx+2])
        j = int(data[idx+3])
        idx += 4
        
        out.append(f"1 1 {n} {m}")
    print("\n".join(out))

if __name__ == '__main__':
    solve()

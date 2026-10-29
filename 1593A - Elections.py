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
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])
        idx += 3
        
        ans_a = max(0, max(b, c) + 1 - a) if a <= max(b, c) else 0
        ans_b = max(0, max(a, c) + 1 - b) if b <= max(a, c) else 0
        ans_c = max(0, max(a, b) + 1 - c) if c <= max(a, b) else 0
        out.append(f"{ans_a} {ans_b} {ans_c}")
    print("\n".join(out))

if __name__ == '__main__':
    solve()

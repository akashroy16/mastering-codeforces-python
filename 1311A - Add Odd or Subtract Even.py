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
        idx += 2
        
        if a == b:
            out.append("0")
        elif a < b:
            if (b - a) % 2 != 0:
                out.append("1")
            else:
                out.append("2")
        else:
            if (a - b) % 2 == 0:
                out.append("1")
            else:
                out.append("2")
    print("\n".join(out))

if __name__ == '__main__':
    solve()

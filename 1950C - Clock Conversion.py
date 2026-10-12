import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        s = data[i]
        h, m = map(int, s.split(':'))
        if h == 0:
            out.append(f"12:{m:02d} AM")
        elif h < 12:
            out.append(f"{h:02d}:{m:02d} AM")
        elif h == 12:
            out.append(f"12:{m:02d} PM")
        else:
            out.append(f"{h-12:02d}:{m:02d} PM")
    print("\n".join(out))

if __name__ == '__main__':
    solve()

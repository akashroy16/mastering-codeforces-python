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
        
        time1 = a - 1
        time2 = abs(b - c) + (c - 1)
        
        if time1 < time2:
            out.append("1")
        elif time2 < time1:
            out.append("2")
        else:
            out.append("3")
    print("\n".join(out))

if __name__ == '__main__':
    solve()

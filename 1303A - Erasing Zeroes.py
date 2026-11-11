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
        s = data[idx]
        idx += 1
        first = s.find('1')
        last = s.rfind('1')
        if first == -1:
            out.append("0")
        else:
            out.append(str(s[first:last+1].count('0')))
    print("\n".join(out))

if __name__ == '__main__':
    solve()

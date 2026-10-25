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
        possible = False
        for j in range(len(s) - 1):
            if s[j] == s[j+1]:
                possible = True
                break
        if possible:
            out.append("1")
        else:
            out.append(str(len(s)))
    print("\n".join(out))

if __name__ == '__main__':
    solve()

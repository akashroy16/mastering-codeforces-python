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
        s_list = list(s)
        swapped = False
        for i in range(1, len(s_list)):
            if s_list[i] != s_list[0]:
                s_list[0], s_list[i] = s_list[i], s_list[0]
                swapped = True
                break
        if swapped:
            out.append("YES")
            out.append("".join(s_list))
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()

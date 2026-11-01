import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    pi = "314159265358979323846264338327"
    out = []
    for i in range(1, t + 1):
        s = data[i]
        count = 0
        for j in range(len(s)):
            if s[j] == pi[j]:
                count += 1
            else:
                break
        out.append(str(count))
    print("\n".join(out))

if __name__ == '__main__':
    solve()

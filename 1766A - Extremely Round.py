import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        n_str = data[i]
        length = len(n_str)
        first_digit = int(n_str[0])
        ans = (length - 1) * 9 + first_digit
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()

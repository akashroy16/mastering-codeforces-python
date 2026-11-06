import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        n = int(data[i])
        res = []
        for third in range(max(1, n - 52), min(26, n - 2) + 1):
            rem = n - third
            for second in range(max(1, rem - 26), min(26, rem - 1) + 1):
                first = rem - second
                if 1 <= first <= 26:
                    res = [chr(ord('a') + first - 1), chr(ord('a') + second - 1), chr(ord('a') + third - 1)]
                    break
            if res:
                break
        out.append("".join(res))
    print("\n".join(out))

if __name__ == '__main__':
    solve()

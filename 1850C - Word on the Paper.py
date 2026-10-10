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
        word = []
        for _ in range(8):
            row = data[idx]
            idx += 1
            for ch in row:
                if ch != '.':
                    word.append(ch)
        out.append("".join(word))
    print("\n".join(out))

if __name__ == '__main__':
    solve()

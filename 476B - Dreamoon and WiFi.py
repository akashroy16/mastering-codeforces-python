import sys

def solve():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    target = sum(1 if c == '+' else -1 for c in s1)
    current = 0
    unknowns = 0
    for c in s2:
        if c == '+':
            current += 1
        elif c == '-':
            current -= 1
        else:
            unknowns += 1
    favorable = 0
    total = 1 << unknowns
    for i in range(total):
        pos = current
        for j in range(unknowns):
            if (i >> j) & 1:
                pos += 1
            else:
                pos -= 1
        if pos == target:
            favorable += 1
    print(f"{favorable / total:.12f}")

if __name__ == '__main__':
    solve()

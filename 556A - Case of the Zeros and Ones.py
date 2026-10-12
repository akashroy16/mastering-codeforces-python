import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    s = data[1]
    c0 = s.count('0')
    c1 = s.count('1')
    print(abs(c0 - c1))

if __name__ == '__main__':
    solve()

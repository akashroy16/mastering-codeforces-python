import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    colors = set(data[2:2+n*m])
    if 'C' in colors or 'M' in colors or 'Y' in colors:
        print("#Color")
    else:
        print("#Black&White")

if __name__ == '__main__':
    solve()

import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    if m >= n and k >= n:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()

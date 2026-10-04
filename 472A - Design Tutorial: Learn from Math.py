import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    
    if n % 2 == 0:
        print(4, n - 4)
    else:
        print(9, n - 9)

if __name__ == '__main__':
    solve()

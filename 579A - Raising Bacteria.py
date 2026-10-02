import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    x = int(data[0])
    print(bin(x).count('1'))

if __name__ == '__main__':
    solve()

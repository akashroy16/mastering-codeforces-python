import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    moves = min(n, m)
    if moves % 2 == 1:
        print("Akshat")
    else:
        print("Malvika")

if __name__ == '__main__':
    solve()

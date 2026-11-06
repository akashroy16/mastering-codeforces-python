import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    
    if m % n != 0:
        print("-1")
        return
        
    div = m // n
    moves = 0
    while div % 2 == 0:
        div //= 2
        moves += 1
    while div % 3 == 0:
        div //= 3
        moves += 1
        
    if div == 1:
        print(moves)
    else:
        print("-1")

if __name__ == '__main__':
    solve()

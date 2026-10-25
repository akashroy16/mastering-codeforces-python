import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    table = data[0]
    hand = data[1:]
    
    possible = False
    for card in hand:
        if card[0] == table[0] or card[1] == table[1]:
            possible = True
            break
            
    if possible:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()

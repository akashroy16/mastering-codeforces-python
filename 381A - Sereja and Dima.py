import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    cards = [int(x) for x in data[1:n+1]]
    
    left = 0
    right = n - 1
    
    sereja = 0
    dima = 0
    turn = 0
    
    while left <= right:
        if cards[left] > cards[right]:
            chosen = cards[left]
            left += 1
        else:
            chosen = cards[right]
            right -= 1
            
        if turn % 2 == 0:
            sereja += chosen
        else:
            dima += chosen
            
        turn += 1
        
    print(sereja, dima)

if __name__ == '__main__':
    solve()

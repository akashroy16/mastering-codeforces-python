import sys
from collections import Counter

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    goals = data[1:1+n]
    
    counts = Counter(goals)
    winner = counts.most_common(1)[0][0]
    print(winner)

if __name__ == '__main__':
    solve()

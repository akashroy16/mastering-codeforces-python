import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        
        if (n // 2) % 2 != 0:
            out.append("NO")
        else:
            out.append("YES")
            half = n // 2
            
            evens = [2 * k for k in range(1, half + 1)]
            odds = [2 * k - 1 for k in range(1, half)]
            odds.append(sum(evens) - sum(odds))
            
            ans = evens + odds
            out.append(" ".join(map(str, ans)))
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()

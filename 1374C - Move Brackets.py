import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        s = data[idx+1]
        idx += 2
        
        balance = 0
        min_balance = 0
        for ch in s:
            if ch == '(':
                balance += 1
            else:
                balance -= 1
            min_balance = min(min_balance, balance)
            
        out.append(str(-min_balance))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()

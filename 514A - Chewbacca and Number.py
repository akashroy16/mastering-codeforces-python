import sys

def solve():
    x = sys.stdin.read().strip()
    if not x:
        return
    
    res = []
    for i, ch in enumerate(x):
        digit = int(ch)
        inverted = 9 - digit
        
        # The leading digit cannot be 0
        if i == 0 and inverted == 0:
            res.append(ch)
        else:
            res.append(str(min(digit, inverted)))
            
    print(''.join(res))

if __name__ == '__main__':
    solve()

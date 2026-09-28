import sys
 
def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    
    for i in range(1, t + 1):
        rating = int(data[i])
        if rating >= 1900:
            out.append("Division 1")
        elif rating >= 1600:
            out.append("Division 2")
        elif rating >= 1400:
            out.append("Division 3")
        else:
            out.append("Division 4")
            
    print('\n'.join(out))
 
if __name__ == '__main__':
    solve()

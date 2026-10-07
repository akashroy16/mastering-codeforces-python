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
        a = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        total_twos = a.count(2)
        if total_twos % 2 != 0:
            out.append("-1")
        else:
            target_twos = total_twos // 2
            curr_twos = 0
            k = -1
            for i in range(n):
                if a[i] == 2:
                    curr_twos += 1
                if curr_twos == target_twos:
                    k = i + 1
                    break
            out.append(str(k))
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()

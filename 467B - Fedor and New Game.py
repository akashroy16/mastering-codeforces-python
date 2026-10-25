import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    x = [int(v) for v in data[3:3+m+1]]
    
    fedor = x[-1]
    friends = x[:-1]
    count = 0
    for player in friends:
        diff_bits = bin(player ^ fedor).count('1')
        if diff_bits <= k:
            count += 1
    print(count)

if __name__ == '__main__':
    solve()

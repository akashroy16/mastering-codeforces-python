import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1:n+1]]
    
    max_len = 1
    curr_len = 1
    for i in range(1, n):
        if a[i] > a[i-1]:
            curr_len += 1
        else:
            if curr_len > max_len:
                max_len = curr_len
            curr_len = 1
    if curr_len > max_len:
        max_len = curr_len
    print(max_len)

if __name__ == '__main__':
    solve()

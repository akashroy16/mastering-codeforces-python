import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    m = int(data[0])
    s = int(data[1])
    
    if s == 0:
        if m == 1:
            print("0 0")
        else:
            print("-1 -1")
        return
        
    if s > 9 * m:
        print("-1 -1")
        return
        
    # Max number
    max_digits = []
    rem = s
    for _ in range(m):
        d = min(9, rem)
        max_digits.append(str(d))
        rem -= d
    max_num = "".join(max_digits)
    
    # Min number
    min_digits = [0] * m
    rem = s - 1
    for i in range(m - 1, 0, -1):
        d = min(9, rem)
        min_digits[i] = d
        rem -= d
    min_digits[0] = rem + 1
    min_num = "".join(map(str, min_digits))
    
    print(f"{min_num} {max_num}")

if __name__ == '__main__':
    solve()

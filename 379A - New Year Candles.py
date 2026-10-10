import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    a = int(data[0])
    b = int(data[1])
    
    hours = a
    went_out = a
    while went_out >= b:
        new_candles = went_out // b
        hours += new_candles
        went_out = new_candles + (went_out % b)
    print(hours)

if __name__ == '__main__':
    solve()

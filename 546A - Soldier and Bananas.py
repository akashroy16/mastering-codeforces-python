import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    k, n, w = int(data[0]), int(data[1]), int(data[2])
    
    total_cost = k * w * (w + 1) // 2
    borrow = max(0, total_cost - n)
    print(borrow)

if __name__ == '__main__':
    main()

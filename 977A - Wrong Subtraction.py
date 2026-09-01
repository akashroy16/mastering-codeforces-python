import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n, k = int(data[0]), int(data[1])
    
    for _ in range(k):
        if n % 10 == 0:
            n //= 10
        else:
            n -= 1
            
    print(n)

if __name__ == '__main__':
    main()

import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n, h = int(data[0]), int(data[1])
    heights = [int(x) for x in data[2:2 + n]]
    
    width = sum(2 if x > h else 1 for x in heights)
    print(width)

if __name__ == '__main__':
    main()

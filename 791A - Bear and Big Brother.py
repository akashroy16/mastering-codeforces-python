import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    a, b = int(data[0]), int(data[1])
    years = 0
    while a <= b:
        a *= 3
        b *= 2
        years += 1
    print(years)

if __name__ == '__main__':
    main()

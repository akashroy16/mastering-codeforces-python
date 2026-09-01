import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    y = int(data[0]) + 1
    
    while len(set(str(y))) != 4:
        y += 1
        
    print(y)

if __name__ == '__main__':
    main()

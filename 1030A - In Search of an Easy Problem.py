import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    if '1' in data[1:]:
        print("HARD")
    else:
        print("EASY")

if __name__ == '__main__':
    main()

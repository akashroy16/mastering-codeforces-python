import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    s = data[1]
    
    remove_count = 0
    for i in range(1, n):
        if s[i] == s[i - 1]:
            remove_count += 1
            
    print(remove_count)

if __name__ == '__main__':
    main()

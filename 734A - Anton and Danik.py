import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    s = data[1]
    
    anton = s.count('A')
    danik = s.count('D')
    
    if anton > danik:
        print("Anton")
    elif danik > anton:
        print("Danik")
    else:
        print("Friendship")

if __name__ == '__main__':
    main()

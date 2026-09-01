import sys

def main():
    username = sys.stdin.read().strip()
    if not username:
        return
    
    unique_chars = len(set(username))
    
    if unique_chars % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

if __name__ == '__main__':
    main()

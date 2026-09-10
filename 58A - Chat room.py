import sys
 
def main():
    s = sys.stdin.read().strip()
    target = "hello"
    idx = 0
    
    for char in s:
        if char == target[idx]:
            idx += 1
            if idx == len(target):
                break
                
    if idx == len(target):
        print("YES")
    else:
        print("NO")
 
if __name__ == "__main__":
    main()

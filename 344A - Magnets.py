import sys
 
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    magnets = input_data[1:]
    
    groups = 1
    for i in range(1, n):
        if magnets[i] != magnets[i - 1]:
            groups += 1
            
    print(groups)
 
if __name__ == "__main__":
    main()

import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    
    current_passengers = 0
    max_capacity = 0
    idx = 1
    
    for _ in range(n):
        a, b = int(data[idx]), int(data[idx + 1])
        current_passengers -= a
        current_passengers += b
        if current_passengers > max_capacity:
            max_capacity = current_passengers
        idx += 2
        
    print(max_capacity)

if __name__ == '__main__':
    main()

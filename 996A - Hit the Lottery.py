n = int(input())
 
count = 0
for bill in [100, 20, 10, 5, 1]:
    count += n // bill
    n %= bill
 
print(count)

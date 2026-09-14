n = int(input())

layers = []
for i in range(1, n + 1):
    if i % 2 == 1:
        layers.append("I hate")
    else:
        layers.append("I love")

print(" that ".join(layers) + " it")

import collections

soln = []

for i in range(20):
    ans = False
    inputs = input().split(' ')
    inputs = [int(input) for input in inputs]
    c = collections.Counter(inputs)
    b = sorted(c.items(), reverse=True)
    # print(b)
    first = 0
    second = 0
    for key, value in b:
        if value >= 4 and first == 0:
            soln.append(int(key) * 4)
            ans = True
            break
        if value >= 2:
            if first == 0:
                first = int(key)
            else:
                second = int(key)
                soln.append(int(first) * 2 + int(second) * 2)
                ans = True
                break
    if not ans: soln.append(-1)

solnString = str(soln[0])

for i in range(1, len(soln)):
    solnString += " " + str(soln[i])

print(solnString)
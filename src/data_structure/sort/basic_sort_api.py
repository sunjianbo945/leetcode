arr = []
for i in reversed(range(10)):
    arr.append(i)

print(f'arr: {arr}')
print(f'create a new sorted arr: {sorted(arr)}')
print(f'create a new reverse sorted arr: {sorted(arr, reverse=True)}')

print(f'arr : {arr}')
arr.sort()
print(f'in position sort use arr.sort() -> arr: {arr}')

arr = []
for i in reversed(range(10)):
    arr.append([i % 3, i])

print(f'arr: {arr}')
print(f'sorted by second key -> arr: {sorted(arr, key=lambda x: x[1])}')
print(f'sorted by first key then second key -> arr: {sorted(arr, key=lambda x: (x[0], x[1]))}')

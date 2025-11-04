def find_longest_run(data):
    if not data:
        return 0
    counter = 1
    maximum = 0
    list_of_long_run = []
    longest_run = data[0]
    # [1, 2, 2, 2, 2, 2, 2]
    for i in range(len(data)-1):
        if data[i] == data[i+1]:
            counter += 1
            maximum = counter
            if i + 1 == len(data) - 1:
                list_of_long_run.append(maximum)
        elif data[i] != data[i+1]:
            list_of_long_run.append(maximum)
            list_of_long_run.append(1)
            counter = 1
    
    return max(list_of_long_run) if len(list_of_long_run) > 1 else list_of_long_run[0]

print()
data = [1, 2, 2, 3, 3, 3, 2, 2]
print(f"Longest run in {data}: {find_longest_run(data)}")

data = ['A', 'A', 'A', 'B', 'C', 'C']
print(f"Longest run in {data}: {find_longest_run(data)}")

data = [5, 5, 5, 5, 5]
print(f"Longest run in {data}: {find_longest_run(data)}")

data = [1, 2, 3, 4, 5]
print(f"Longest run in {data}: {find_longest_run(data)}")

data = []
print(f"Longest run in {data}: {find_longest_run(data)}\n")

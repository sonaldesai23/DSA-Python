# Add 2 nested lists (like 2D array)
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list3 = []

print("List 1 contains")  # Showing elements of list1
i = 0
while i < len(list1):
    j = 0
    while j < len(list1[i]):
        print(list1[i][j], end="\t")
        j += 1
    print()
    i += 1

print("List 2 contains")  # Showing elements of list2
i = 0
while i < len(list2):
    j = 0
    while j < len(list2[i]):
        print(list2[i][j], end="\t")
        j += 1
    print()
    i += 1

# Performing addition and appending to list3
i = 0
while i < 3:
    j = 0
    list3.append([])
    while j < 3:
        sum = list1[i][j] + list2[i][j]
        list3[i].append(sum)
        j += 1
    print()
    i += 1

print("\nList 3 contains")  # Showing elements of list3
i = 0
while i < len(list3):
    j = 0
    while j < len(list3[i]):
        print(list3[i][j], end="\t")
        j += 1
    print()
    i += 1


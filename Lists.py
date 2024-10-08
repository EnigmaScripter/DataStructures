list1 = [1, 2, 3, 4, 5]

list1.remove(3)
print(f"Index of item 4 equal: {list1.index(4)}")
list1.append(6)
print(f"Index of item 4 equal: {list1.index(4)}")
list1.insert(2, "Mohamed")
list1.reverse()
print(list1[0])

print(f"Index of item 4 equal: {list1.index(4)}")

print(list1.pop(1))
del list1[0]
print(list1)
print(f"Index of item 4 equal: {list1.index(4)}")

list1.clear()
print(list1)
del list1
print(list1)


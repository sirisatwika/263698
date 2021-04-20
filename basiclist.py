numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)
numbers[0] = 111
print("\nPrevious list content:", numbers) 
numbers[1] = numbers[4]
print("Previous list content:", numbers)
print("\nList's length:", len(numbers))
del numbers[1]
print("New list's length:", len(numbers))
print("\nNew list content:", numbers)
print(numbers[-1])
print(numbers[-2])
print(len(numbers))
print(numbers)
numbers.append(4)
print(len(numbers))
print(numbers)
numbers.insert(0, 222)
print(len(numbers))
print(numbers)


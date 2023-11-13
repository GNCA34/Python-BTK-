from tkinter import N


numbers=[1,10,5,16,4,9,10]
letters=['a','g','s','b','y','a','s']
val=min(numbers)
val=max(numbers)
val=max(letters)
val=min(letters)
print(val)

val=numbers[3:6]
val=numbers[:3]
val=numbers[4:]
numbers[4]=40
print(val)

numbers.append(49)
numbers.insert(3,78)
# numbers.insert(-1,52)
numbers.append(67)
print(numbers)
numbers.insert(-2,3)
numbers.pop()
numbers.remove(9)
numbers.sort()
numbers.reverse()
letters.reverse()
print(letters)
print(numbers)
print(len(numbers))
print(len(letters))
print(numbers.count(10))
print(letters.count('a'))

numbers.clear()
print(numbers)


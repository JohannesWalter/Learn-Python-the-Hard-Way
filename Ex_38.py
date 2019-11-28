# Exercise 38 - Doing things to Lists

lst = []
number = 0
while number < 10:
    lst.append(number)
    number += 1

print(lst)
lst.insert(2, "chocolate")
print(lst)
print(lst[3:6])
lst.insert(8, "bananarama")
print(lst[2:9])
print(lst[-3:-1])
lst.pop(2)
print(lst)
lst.pop()
print(lst)
lst.remove("bananarama")
del lst[2]
print(lst)
lst.clear()
print(lst)
lst = ["apple", "banana", "coffee", "beer"]

listy = lst

lst.pop()

print(listy)

lst_copy = lst.copy()

lst.pop()

lst_copy

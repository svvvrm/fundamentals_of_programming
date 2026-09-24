a = 1000
b = a
c = int("1000")
# c = None

print("Типы:", type(a), type(b), type(c))
print("Идентификаторы:", id(a), id(b), id(c))
# True expected
print("a == b:", a == b)
# True expected
print("a is b:", a is b)
# True expected
print("a == c:", a == c)
# False expected
print("a is c:", a is c)

# # True expected
# print("c is None:", c is None)

first = "python"
second = "py" + "thon"

print(first == second)
print(first is second)
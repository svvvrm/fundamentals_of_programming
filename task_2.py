a = 1000
b = a
c = int("1000")

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
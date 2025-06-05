from pythonic_db_manipulation import Table

tb = Table("test", ["id", "name", "age"])

print(tb)

tb.push([1, "John", 25])
tb.push([2, "Jane", 30])
tb.push([3, "Lucy", 12])
tb.push([4, "Marco", 56])
tb.push([5, "Mario", 16])
tb.push([6, "Luiji", 42])

print(tb)

tb.pop()

print(tb)

tb.pop(1)

print(tb)

print(tb.get())
print(tb.get(1))

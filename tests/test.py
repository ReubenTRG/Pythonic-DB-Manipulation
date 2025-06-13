from pythonic_db_manipulation import Table

tb1 = Table("A", ["id", "name"])
tb1.push([1, "Alice"])
tb1.push([2, "Bob"])
tb1.push([3, "Sam"])

print(tb1.pop())

print(tb1)

tb2 = Table("B", ["id", "name"])
tb2.push([2, "Bob"])
tb2.push([3, "Charlie"])

print(tb1 + tb2)  # Union
print(tb1 & tb2)  # Intersection
print(tb1 - tb2)  # Difference


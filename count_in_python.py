# 'Find' is a method of strings. It returns the
# the lowest index of the string where the substring is found
an_str = "hello world"
print(an_str.find("e"))
print(an_str.find("or"))

# Count is a method on str, list, tuple to count the number of
# occurrences of an element.
a_list = [1, 2, 3, 4, 2, 4, 2]
another_list = ['b', 'h', 'l', 'h']

print(a_list.count(2))
print(another_list.count('h'))

an_str = "hello world"
print(an_str.count("o"))

print(dir(tuple))
print(dir(set))

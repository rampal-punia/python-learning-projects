# class SomeClass(str):
#     def __eq__(self, other):
#         return (
#             type(self) is SomeClass
#             and type(other) is SomeClass
#             and super().__eq__(other)
#         )

#     # When we define a custom __eq__, Python stops automatically inheriting the
#     # __hash__ method, so we need to define it as well
#     __hash__ = str.__hash__


# some_dict = {'s': 42}

# s = SomeClass('s')
# some_dict[s] = 40
# print(some_dict)

a_dict = {'s': 42, 's': 40}
print(a_dict)

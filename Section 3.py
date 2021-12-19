# x = (1, 2, (3, 'John', 4), 'Hi')
#
# print(x[2][2])

#Exercise: Odd Tuples
#
# def oddTuples(aTup):
#     i = 0
#     NewTup = ()
#     for t in aTup:
#         i += 1
#         if i % 2:
#             NewTup = NewTup + (t,)
#
#     return NewTup
#
# oddTuples(('I', 'am', 'a', 'test', 'tuple'))


#Exercise 3

listA = [100, 0, 1, 4, 4, 1, 6, 3, 4]
listB = ['x', 'z', 't', 'q']

print(listA.reverse())
print(listA)
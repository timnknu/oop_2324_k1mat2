a = ['a', -125, 'hello', 81]

# for el in a: # b = iter(a)
#     print(el)

i = 0
while i < len(a):
    print(a[i])
    i += 1
    #del i


b = iter(a)
print(b)
#print( '\n'.join( dir(b) ) )

print(next(b)) # print(b.__next__())
print(next(b)) # print(b.__next__())
print(next(b)) # print(b.__next__())
print(next(b)) # print(b.__next__())
print(next(b)) # print(b.__next__())
print(next(b)) # print(b.__next__())




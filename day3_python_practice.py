# using enumerate
a = ["apple","banana","cat"]
for i,v in enumerate(a):
    print(i,v)

b=["a","b","c"]
r = list(enumerate(b))
print(r)

c = [2,4,6,8,10]
for i,v in enumerate(c,1):
    print(i,v)

#zip() in python
names = ["John","Emma","Liam"]
scores = [78,92,85]
result = zip(names, scores)
print(dict(result))


c = [10,15,20,25,30]
squares = map(lambda x:x** 2,c)
res = zip(c, squares)
print(dict(res))

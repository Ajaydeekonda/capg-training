d1 = {}
d2 = {'spam':2,'inbox':3}
d3 = {'food':{'ham':1,'egg':2}}
d4 = dict(name = 'bob',age=40)
keyslist = ['ajay','anirudh']
valslist = [22,23]
d5 = dict(zip(keyslist,valslist))
d6 = dict.fromkeys(['a','b'])


# print(d1,"\n",d2,"\n",d3,"\n",d4,"\n",d5,"\n",d6)

print(d2.keys())
print(d3.values())
print(d4.items())
print(d2.get('primary',"N/A"))
print(d2.update({'spam':3,'inbox':4,'primary':10}))
print(d2)
print(d2.pop('spam'))
print(len(d5))


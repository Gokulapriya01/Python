import sys

"""let="abcdefghijklmnop"
print(let[0:6])
print(let[0::2])
print(let[-5:-1])
print(let.upper())
print(let.capitalize())
print(let.split())
print(let[0])
print(sys.version)
print(sys.int_info)
print(len(let))
st=let+"qrstuvwxyz"
print(st)
print(3*st)
a="sam paul"
b=a.replace("paul","brook")
print(a,b)
print(a.find('au'))
print(let.find('m'))
print(a.find('ue'))"""""

"""""
#Tuple:
R=(1,5,9,4,7,3,8)
t1=("did",10.2,5)
print(t1[0],t1[1])
print(t1[-1])
t2=t1+R    #concatenation
print(t2)

print(t2[2:7]) #Slicing
print(t2[-7:-1])
print(sorted(R))
print(R)
N=(1,2,("pop","rock"),(3,4),("di",1.2,3))
print(N[2][1],N[3])
print(N[4][1])

for data in N:
    print(data)"""""

""""
#Lists:
L=["Michael JJ",10.2,7,6,"Pam Brook"]
Con=L+["Pop",1,5.8]
print(Con)
L.extend(["pop",17])
print(L) #adds multiple elements with diff index(ex. adds 2 elements with 2 different indexes)
L.append(["paul",88])

print(L)
print(L[4].split())
#help(L)
L.reverse()
print(L)
L.pop()
print(L)
L.remove(7)
print(L)
"""

""""
#Dictionaries:
dict1={"thriller":1992,200:800,"Black rock":1980,"dark side":1973}
print(dict1)
dict1['Graduation']=2025
dict1['The book']=2020
dict1['Dark']=2021
print(dict1)
del(dict1['The book'])
print(dict1)
print('thriller' in dict1)
print(dict1.keys())
print(dict1.items())
print(dict1.values())
print(dict1.get('Dark'))
"""

""""
#Sets:
al1={"pop","thriller","soul","pam brook","Sam Paul", "R&B", "disco"}
L=["Michael JJ",10.2,7,6,"Pam Brook"]
set2=set(L)
print(set2)
set2.add("NSYNC")
print(set2)
set2.remove("NSYNC")
print(set2)
print(10.2 in set2)
al2={"Back black","rock","soul","The dark side", "R&B", "disco"}
print(al1.union(al2))
print(al1.intersection(al2))
print(al1.issuperset(al2))
print(al1.difference(al2))
print(al1.isdisjoint(al2))
print(al1.symmetric_difference(al2))
print(al1.difference_update(al2))
"""


dates = [1982,1980,1973]
#N = len(dates)

for i in dates:
    print(i)


dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])          

dates = [1982,1980,1973]
#N = len(dates)

for i in enumerate(dates):
    print(i)

for dates[0] in range(len(dates)): 
    dates[0]=2000
    print(dates)
    print(dates[0],dates[1])
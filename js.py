
data="""{"ID":"D899","lname":"sam", "name":"Rose","course":"MS"}"""
import json
my=json.loads(data)
print(data)
for k,v in my.items():
    print(k,":",v)

fp=open("/Users/gokulapriyas/Downloads/bas")
my1=json.load(fp)
print(my1)
for k,v in my1.items():
    print(k,":",v)
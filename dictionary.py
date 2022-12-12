"""month={"Jan" :1, "Feb": 2, "Mar": 3,"Apr":4,"May":5,"Jun":6}
print(month)
print(type(month))
d=dict((("one",1),("two",2),("three",3),("four",4)))
print(d)
print((d["four"]))


c=dict((("sudharsan",12215959),("subash",12215948),("nithish",12215930),("harsh",1221493)))
print(type(c))
print(c["sudharsan"])

d={"Tamil":90,"English":90,"Maths":85,"Science":89,"social":90}


print(month.get("Feb"))
print(month.get("Sep"))
dict1={"name":"Jay","number":514,"age":12}
print(dict1)
dict1["name"]="Krithika"
print(dict1)
dict1["age"]=25
print(dict1)
# Zip function add the two tuple like a matrix

a=("John","Charles","Mike")
b=("Jenny","Christy","Monica")
x=zip(a,b)
print(tuple(x))
y=zip(b,a)
print(dict(tuple(y)))
# sorted list and done some operation based on the import items in the list and sorting the items of the dictionary
list1=[10,20,30] #First list
list2=["Tem","Twenty","Thirty"]
mydict=dict((zip(list1,list2)))
print(mydict)
print(sorted(mydict))
print(mydict.items())
print(sorted(mydict.items()))
p=[10,20,30]
print(tuple(zip(list1,list2)))









"""


#Program to convert keys to values andvalues  to keys
#Notethe same value 10 for keys 1 and 5
#First timethe entry gets cretated and the second timethe value gets updatted
data1=input("ddata1:")
data2=input("data2:")
list1=data1.split(",")
list2=data2.split(",")
dict1=dict(zip(list1,list2))
d3=dict()
for key in dict1:
    d3[dict1[key]]=key
print("before exchange:",sorted(dict1.items()))
print("after exchange:",sorted (d3.items()))

troupe={("Clease","John"):[1,2,3],("Charman","Graham"):[4,5,6],("Idle","Eric"):[7,8,9],("Jones","Terry"):[10,11,12],("Gilliam","Terry"):[13,14,15],("Palin","Michael"):[16,17,18]}

print(sorted(troupe.items()))
print(sorted(troupe))
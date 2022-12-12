def mysum(*args):
    sum1=0
    for i in args:
        sum1=sum1+i
    return (sum1)
print(mysum(1,2,3,4,5,6,7))

def largestnumber(*numbers):
    m=numbers[0]
    for num in numbers:
        if num>m:
            m=num
    print("largest:",m)
largestnumber(1,2,3,4)

x=lambda a:a+10
print(x(5))
x=lambda a,b:a+b
print(x(6,4))
l1=[1,5,7,8,9]

def addition(n):
    return n+n
numbers=[1,2,3,4]
result=map(addition,numbers)
print(list(result))



numbers1=[1,2,3,4]
result=map(lambda x: x+x,numbers1)
print(list(result))

def fun(variable):
    letters=["a","e","i","o","u"]
    if variable in letters:
        return True
    else:
        return False
sequence["g","e","w","e","i","z"]
filtered=filter(fun,sequence)
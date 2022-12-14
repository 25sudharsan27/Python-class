# Multiplication table for any number is available here




class Tables():
    def __init__(self,t,r):
        self.t=t
        self.r=r
    def mul(self):
        print("------------------------")
        i=0
        for i in range(self.r):
            i=i+1
            print(i,"x",self.t,"=",int(i*self.t))
        print("------------------------")
    def addi(self):
        print("------------------------")
        i=0
        for i in  range(self.r):
            i=i+1
            print(i,"+",self.t,"=",int(i+self.t))
        print("------------------------")
    def dif(self):
        print("------------------------")
        i=0
        for i in range(self.r):
            i=i+1
            print(i,"-",self.t,"=",int(i-self.t))
        print('------------------------')
    def div(self):
        print("------------------------")
        i=0
        for i in range(self.r):
            i=i+1
            print(i,"/",self.t,"=",int(i/self.t))
        print('-------------------------')

for i in range(10000000):
    t = int(input("Enter which table you want :"))
    r = int(input("How many rows you want :"))
    print('1.Addition')
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

    ch=int(input("Enter the choice: "))
    if ch==1:
        ob=Tables(t,r)
        ob.addi()
    if ch==2:
        ob=Tables(t,r)
        ob.dif()
    if ch==3:
        ob=Tables(t,r)
        ob.mul()
    if ch==4:
        ob=Tables(t,r)
        ob.div()
    else:
        print("Please enter your correct choice next time")
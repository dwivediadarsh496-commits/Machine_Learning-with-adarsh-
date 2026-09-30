'''
class microemployees:
    company = "microsoft"
    def __init__(self,Name,salary,pin):
        self.Name = Name
        self.salary = salary
        self.pin = pin

p = microemployees("adarsh",120000,25004)  
print(p.Name,p.salary,p.pin)     
r = microemployees("manvendra",15555,85554)
print(r.Name,"      ",r.pin)
 
class calculator:
    def __init__(self,n):
        self.n = n

    def squre(self) :       
        print(f" the squre of  n is {self.n*self.n}")

    def cube(self)  : 
        print(f" the cube of n is {self.n*self.n*self.n}")

a = calculator(6)
a.cube()
'''
# train running status and more .....
import random
class train :
    def __init__(self,train_num):
        self.train_num = train_num

    def book(self,fro,to):
    
        print(f"the ticket is booked from train num {self.train_num} from {fro} to {to}") 

    def fare(self,fro,to) :
        print(f"the fare of train no. {self.train_num} from {fro} to {to} is {random(108,255)}") 

    def getstatus(self) : 
        print(f"train no {self.train_num} is running on time ")   



t = train(12399)
t.book("Rampur", "Delhi")

t.fare("Rampur", "Delhi")




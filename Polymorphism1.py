class Student:
    def _init_(self,name,age):
        self.name=name 
        self.age=age
    @classmethod
    def admission(cls,roll,name):
        return cls(name,roll)
s1=Student.admission(101,'Rupali')
print(s1.name)
print(s1.age)

s2=Student.admission(102,'Siddharth')
print(s2.name)
print(s2.age)


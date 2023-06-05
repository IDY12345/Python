class Poly :    
    def area(self,l,b):
        a=l*b
        print("Area of Rectangle :",a)
class Rect(Poly) :
    def area(self,l,b):
        p=2*(l+b)
        print("Perimeter Of Rectangle :",p)
print("Enter length and Breadth of the rectangle")
l=int(input())
b=int(input())

k=Poly()
m=Rect()
k.area(l,b)
m.area(l,b)
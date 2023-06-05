class class_room:
    def _init_(self,class_no):
        self.class_no=class_no
    def display_class_room(self):
        print("This is class no",self.class_no)
class lab:
    def _init_(self,lab_no):
        self.lab_no=lab_no
    def display_lab_no(self):
        print("This is lab no",self.lab_no)
class department:
    def _init_(self,lab_no,class_no):
        self.lab=lab(lab_no)
    def display_dept(self):
        print("Department contains lab")
        self.lab_display_lab()
        print("Department Contains Classroom")
        self.display_class_room()
        d=department(101,201)
        d.display_dept()
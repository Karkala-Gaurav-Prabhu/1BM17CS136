class student:

    def __init__(self, age = 0, marks = 0, stud_id = ""):
        self.age = age
        self.marks = marks
        self.stud_id = stud_id 

    def validate_age(self):
        if self.age <= 0:
            print("Age cannot be less than 0.")
            return False
        else:
            print("Age succesfully Validated.")
            return True

    def validate_marks(self):
        if self.marks < 0 or self.marks > 100:
            print("Marks should be in the range 0 to 100.")
            return False
        else:
            print("Marks succesfully Validated.")
            return True

    def check_qualification(self):
        if (self.validate_age() is True and self.validate_marks() is True):
            if(self.marks >= 65 and self.age >=20):               
                return True
            else:
                return False

        else:
            return False

    def setter(self, stud_id, age, marks):
        self.age = age
        self.marks = marks
        self.stud_id = stud_id

    def getter(self):
        print("Student ID: ", self.stud_id)
        print("Age: ", self.age)
        print("Marks: ", self.marks)


stud = input("Enter Your Student ID: ")
age = int(input("Enter Your Age: "))
marks = int(input("Enter Your Marks: "))

stud1 = student()
stud1.setter(stud, age, marks)
stud1.getter()
if(stud1.check_qualification() is True):
    print("You Have Been Qualified To Be Admitted.")
else:
    print("You Are Not Qualified.")

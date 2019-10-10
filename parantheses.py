class Validate:
     def __init__(self, string):
          self.string = string

     def isvalid(self):
          count = 0
          for parantheses in string:
               if parantheses == '(':
                    count += 1
               elif parantheses == ')':
                    count -= 1
               elif parantheses == '{':
                    count += 2
               elif parantheses == '}':
                    count -= 2
               elif parantheses == '[':
                    count += 3
               elif parantheses == ']':
                    count -= 3

          if count == 0 :
               print("Valid")
          else:
               print("Invalid")

string = input("Enter A String Of Parantheses")

val = Validate(string)
val.isvalid()

'''
Output:
Enter A String Of Parantheses: {()}
Valid
'''

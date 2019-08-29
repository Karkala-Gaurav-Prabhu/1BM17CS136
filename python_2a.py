def numList(orderedList, elementToSearch):
     if elementToSearch in orderedList:
          return True
     else:
          return False
          

lst = []

size = int(input("Enter size of array: "))

for i in range(0, size):
     ele = int(input("Enter element: "))
     lst.append(ele)

search = int(input("Enter element to search: "))

if(numList(lst, search)):
     print("Element", search," exists in the List")
else:
     print("Element", search," does not exist in the List")

n = int(input("Enter the no of fibonacci nos to generate "))
a = 0
b = 1
print(a)
print(b)
for i in range(2,n):
     c=a+b
     a=b
     b=c
     print(c)

     
'''
OUTPUT
Enter the no of fibonacci nos to generate 6
0
1
1
2
3
5
'''

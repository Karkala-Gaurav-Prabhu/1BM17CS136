from random import randint

while True:
    a = []
    i = 1
    num = 3
    len = int(input("Enter Length of password to be generated: "))
    for i in range(0,len):
        if num == 3:
            num = int(randint(1,2))
        elif num == 2:
            while True:
                num = int(randint(1,3))
                if num != 2:
                    break
        elif num == 1:
            num = int(randint(2,3))
        
        if num == 1:
            n = randint(97,122)
            a.append(chr(n))
            string1 = "".join(a)
        elif num == 2:
            n = randint(65,90)
            a.append(chr(n))
            string1 = "".join(a)
        elif num == 3:
            n = randint(33,63)
            a.append(chr(n))
            string1 = "".join(a)
        
    print(string1)
    ask = str(input("Do You Want To Generate New password?(y/n)"))
    if ask == 'n':
        break
            
    
        

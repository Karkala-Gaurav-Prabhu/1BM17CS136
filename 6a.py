prime = open('happy-no.txt', 'r')
happy = open('prime_no.txt', 'r')

prime_string = prime.read()
happy_string = happy.read()

prime_no = prime_string.split(",")
happy_no = happy_string.split(",")

prime_no[-1] = prime_no[-1].strip()
happy_no[-1] = happy_no[-1].strip()

overlap = []

for number in prime_no:
     if number in happy_no:
          overlap.append(number)

print("The overlapping numbers are: ",overlap)

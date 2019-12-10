
x = 13
y = True

for i in range(2, x):
 if (x % i)==0:
  y = False

if y:
 print("{:d} is a prime number".format(x))


#Rosalind Conditions and Loops 

inp = open('rosalind_ini4.txt', 'r')
data = inp.read().split()

a = int(data[0])
b = int(data[1])


if(a%2 == 0):
	z = a + 1
else:
	z = a 
if(b%2 !=0):
	b = b + 2

x = (b - a)/2
i = 0 
y = 0 


while(i < x):
	y = y + z 
	z = z + 2 
	i = i + 1
 

print(y) 
inp.close()
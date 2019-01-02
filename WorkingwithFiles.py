
#Rosalind intro problem 5 working with files 

inp = open('rosalind_ini5.txt', 'r')
data = inp.read().split('\n') #split on new line characters 
output = open('rosalind_out5.txt', 'w')

i = 1 
string = ""
a = len(data) 

while(i < a):
	string = data[i]
	i = i+2
	output.write(string)
	output.write('\n')
	
	

	
	
	
output.close()	
inp.close()
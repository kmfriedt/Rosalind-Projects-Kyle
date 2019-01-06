#transcribe DNA to RNA 

#DNA to RNA 

inp = open('rosalind_rna.txt', 'r') 
output = open('RNA.txt', 'w')

data = inp.read() #read the file as one long string 

chars = [] # create empty list


for char in data: #make a list of the individual chars 
	chars.append(char)
#print(chars)

#get teh length of the list 
length = len(chars) 

print(length) 

i = 0 
while(i < length): #iterate through list, find all T's and replace with U's 
	
	for item in chars:
		if(chars[i] == 'T'):
			chars[i] = 'U'
	i = i + 1
string = ""

for item in chars:
	string = string + item 
	
print(string) 

output.write(string) 

output.close() 	
	
inp.close() 
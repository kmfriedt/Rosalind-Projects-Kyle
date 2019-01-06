

inp = open('rosalind_revc.txt', 'r') 
output = open('RNAcompOutput.txt', 'w')

data = inp.read() #read the file as one long string 

def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str 



revdata = reverse(data)
chars = [] # create empty list

for char in revdata: #make a list of the individual chars 
	chars.append(char)


#get the length of the list 
length = len(chars) 

 

i = 0 
while(i < length): #iterate through list, complement 
	
	if(chars[i] == 'T'):
		chars[i] = 'A'
	elif(chars[i] == 'A'):
		chars[i] = 'T'
	elif(chars[i] == 'G'):
		chars[i] = 'C'
	elif(chars[i] == 'C'):
		chars[i] = 'G'	
	i = i + 1
	
string = ""

for item in chars:
	string = string + item 
	
print(string) 

output.write(string) 

output.close() 	
	
inp.close() 
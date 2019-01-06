#DNA to RNA 

inp = open('rosalind_dna.txt', 'r') 

data = inp.read() #read the file as one long string 

chars = [] # create empty list

for char in data: #make a list of the individual chars 
	chars.append(char)
#print(chars)

#create a character frequency dictionary 
chfreq = {} #empty dictionary 

for ch in chars:
	chfreq[ch] = chfreq.get(ch,0) + 1 # if ch is not in dict add it, if it is increase its value by 1 
	
#NEED TO PRINT IN ORDER A C G T NO MATTER WHAT ORDER THEY APPEAR
	
a = chfreq['A']
c = chfreq['C']
g = chfreq['G']
t = chfreq['T'] 

print(a,' ',c,' ',g,' ',t) 
	

	
inp.close() 
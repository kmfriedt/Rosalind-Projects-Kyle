#Rosalind Dictionaries Problem

inp = open('rosalind_ini6.txt', 'r')
data = inp.read().split() #split on white space get a list of words 

wordfreq = {} #create an empty dictionary 

for word in data:
	wordfreq[word] = wordfreq.get(word,0) + 1 #for each item in the list data add it to the dictionary
				#if the key is not in the dictionary set value to 1. if it is in the dictionary increment its value
	
	
for word,count in wordfreq.items():
	print(word,count)
	
inp.close()
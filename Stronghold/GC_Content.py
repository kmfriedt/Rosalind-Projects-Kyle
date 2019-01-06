

# too many variables on memory 
# break into functions? 

inp = open('rosalind_gc.txt', 'r') 

data2 = []
for line in inp: #read each line in the file and remove newline characters 
	line = line.rstrip()
	data2.append(line)
	

str = ""
for item in data2:#read all the items in data into a long string 
	str = str + item
	
data=[]
data=str.split('>')#split the long string on the '>' 

print(data) 
del data[0] 

dict = {} #empty dictionary 

datalength = len(data)
i = 0
s = ""
s1 = ""
s2 = ""
nt_list = []

while(i < datalength): #set Id as keys
	s = data[i] 
	s1 = s[:13]
	dict[s1] = 0.0
	s2 = s[13:]
	nt_list.append(s[13:])
	i = i + 1
print(dict)
#print(nt_list)


gc_list = []
for item in nt_list:#organize the gc_content percentages into a list  
	gc_count = 0 
	gc_percent = 0.0 
	for nt in item:
		if nt == 'G' or nt == 'C':
			gc_count = gc_count + 1 
	if gc_count != 0:
		gc_percent = gc_count / len(item) *100
	else:
		gc_percent = 0.0 
	gc_list.append(gc_percent)

	
	
print(gc_list) 
	
# j = 0 
# length = 0 
# n = 0.0 


# while(j < datalength):#caculate gc_content and put into gc_list 
	# length = len(data[j])

	# gc_count = 0
	# for nt in data[j]:
		# if(nt == 'G' or nt == 'C'):
			# gc_count = gc_count + 1 
			 
	# if n != 0:
		# n = gc_count / length * 100
	# else:
		# n = 0
	# gc_list.append(n)
	# j = j + 2
	

	
	
k = 0 
for key in dict.keys():#set the values to the keys 
	dict[key] = gc_list[k]
	k = k + 1 
	
largest = None 
tag_key = None 

for tag,content in dict.items():#find the largest gc_content key / value pair and print
	if largest is None or content > largest:
		largest = content 
		tag_key = tag 
		
print(tag_key)
print(largest) 
	


	
inp.close() 
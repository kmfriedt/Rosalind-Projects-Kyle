

inf = open('rosalind_ini3.txt', 'r')

data = inf.read() #this will read it all as one long string
inp = open('rosalind_ini3.txt', 'r')
data2 = inp.read().split() #splits data on white space, list of the data split on white space 


print(data2)
string = ""
string = data2[0] 


print(string) 
a = int(data2[1])
b = int(data2[2])
c = int(data2[3])
d = int(data2[4])


s1=""
s2=""
i = a
j = c 
while(i <= b): 
	s1 = s1 + string[i]
	i = i + 1 
while(j <= d):
	s2 = s2 + string[j]
	j = j + 1 
	
print(s1,s2) 


inf.close()
inp.close() 
f=open("File.txt",'r') # reading tab seprated txt file
p=open("Generated.txt",'w')
f.readline() #avoiding headings
identity = f.readline().strip('\n')
count = 1
while identity:
	split_identity = identity.split("\t")

	#details
	coder = split_identity[2]
	name = split_identity[0]
	email = split_identity[1]
	code = '+'.join(name.split())
	
	#DONT FORGET to change foldername FOLDER with event name before adding participant value
	a="{ value: '"+name+" | "+email+"', data: '<a href=\"https://s3.ap-south-1.amazonaws.com/ec4bdiw/"+str(count)+'_'+str(code)+".jpg\" target=\"_blank\" download=\"https://s3.ap-south-1.amazonaws.com/ec4bdiw/"+str(count)+'_'+str(code)+".jpg\">Download</a>'},\n"
	
	count+=1
	
	p.write(a)
	identity = f.readline().strip('\n')
	
f.close()
p.close()

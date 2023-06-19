inp = input("Enter the line: ")
inp_list = inp.split()
fs = open('file.txt', 'a')
for i in range(len(inp_list)):
	fs.write(inp_list[i] + " ")
	
fs.write("\n")
fs = open('file.txt', 'r')
fs.read()

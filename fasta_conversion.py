f = open('CTGATC.fastq')

lines_list = f.readlines()
seqs_list = []

count = 0
while count < len(lines_list)-1:
	possible_sequence = lines_list[count+1].rstrip()
	if lines_list[count][0:1] == '@':
		if possible_sequence[0:1] != '@':
			seqs_list.append(possible_sequence)
	count +=1
print seqs_list

#Wilder was here



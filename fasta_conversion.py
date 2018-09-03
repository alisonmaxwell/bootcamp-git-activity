import matplotlib.pyplot as plt

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
#print seqs_list

def hamdist(str1, str2):
   """Count the # of differences between equal length strings str1 and str2"""
   diffs = 0
   for ch1, ch2 in zip(str1, str2):
       if ch1 != ch2:
           diffs += 1
   return diffs

ham_count = 0
distances = []
while ham_count < len(seqs_list)-1:
	i = seqs_list[ham_count]
	j = seqs_list[ham_count+1]
	distances.append(hamdist(i,j))
	ham_count += 1 

plt.hist(distances, bins = 10)
plt.show()

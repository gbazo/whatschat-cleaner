filenames = ["data"]
cwboolean = True
othersboolean = True

for names in filenames:
	file_handle = open(names + "out.txt")
	print(names + "out.txt has been opened")
	fcw = open(names + "GB.txt", 'w')
	fothers = open(names + "sep.txt", 'w')
	for line in file_handle:
		if(line.startswith("Gabriel Bazo")):
			if(cwboolean):
				fcw.write("|\n")
				othersboolean = True
				cwboolean = False
			fcw.write(line)
		else:
			if(othersboolean):
				fothers.write("|\n")
				cwboolean = True
				othersboolean = False
			fothers.write(line)
		#print(line)
file_handle.close()
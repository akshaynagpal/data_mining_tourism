import csv
with open('result1to12.csv','wb') as outcsvfile:
	filewriter = csv.writer(outcsvfile)
	with open('crime1to12.csv','rb') as csvfile:
		filereader = csv.reader(csvfile)
		for row in filereader:
			if row[2]=="TOTAL IPC":
				print str(row[0]) + " " + str(row[1]) + " " + str(row[17])
				filewriter.writerow([str(row[0]),str(row[1]),str(row[17])])

import csv

wfile=open("D:/rakuten/hotelMaster.csv","wb")
writer=csv.writer(wfile)

for num in range(0,1):
	ifile=open("D:/rakuten/travel03_hotelMaster_20140930.txt","r")
	idata=csv.reader(ifile,delimiter="\t")
	for line in idata:
		writer.writerow(line)
	ifile.close()
wfile.close()

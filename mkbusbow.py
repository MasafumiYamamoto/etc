###make bow list

def main():
	import csv
	import textedit
	import time
	import collections
	import glob

	stopfile=open("D:/Lresult/NV_s5/subrev_1000.csv","r")
	stopdata=csv.reader(stopfile)
	stoplist=collections.Counter()
	for line in stopdata:
		stoplist[line[0]]=1
	stopfile.close()

	buslist=glob.glob("D:/Lresult/NVbus/*")
	print len(buslist)

	##make document bow
	for bus in buslist:
		dfile=open(bus,"r")
		ddata=csv.reader(dfile)
		busname=""
		wlist=collections.Counter()
		for line in ddata:
			busname=line[2]
			if(line[0] not in stoplist):
					te=line[5]
					doc=textedit.textedit(te)
					dlist=doc.split()
					for t in dlist:
						wlist[t]=wlist[t]+1
		wfile=open("D:/Lresult/NVbusbow/"+busname+".csv","wb")
		writer=csv.writer(wfile)
		writer.writerow(["word","num"])
		writer.writerows(wlist.items())
		wfile.close()
		dfile.close()

if __name__ == '__main__':
	main()

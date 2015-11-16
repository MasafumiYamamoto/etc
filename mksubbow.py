###make bow for each line

def main(pas_):
	import collections
	import csv
	import textedit
	import time

	pas=str(pas_)

	print "mkcorpus_start",time.ctime()
	##make documents
	dnum=0
	subfile=open(pas+"subrev_1000.csv","r")
	subdata=csv.reader(subfile)
	subdata.next()
	for line in subdata:
		te=line[5]
		doc=textedit.textedit(te)
		dlist=doc.split()
		wlist=collections.Counter()
		for t in dlist:
			wlist[t]=wlist[t]+1
		wfile=open(pas+"subrevbow/"+line[0]+".csv","wb")
		wri=csv.writer(wfile)
		wri.writerow(["word","num"])
		wri.writerows(wlist.items())
		wfile.close()
	subfile.close()


if __name__ == '__main__':
	#print "pas"
	pas_="D:/Lresult/NV_s5/"
	main(pas_)

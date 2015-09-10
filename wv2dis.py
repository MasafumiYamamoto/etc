import csv
import numpy
import glob
import os
import time
import collections


n=0
l=0
for num in range(0,1):
	flag=0
	print time.clock()
	ifile=open("hoeg.csv","r")
	idata=csv.reader(ifile)
	for line in idata:
		wfile=open("re.csv","wb")
		#wfile=open("simresult/"+line[0]+".csv","wb")
		writer=csv.writer(wfile)
		idic=collections.Counter(line[2:])
		ilen=numpy.linalg.norm(idic.values())
		max=0
		pre=""
		rfile=open("hoeg.csv","r")
		rdata=csv.reader(rfile)
		for row in rdata:
			if(line[0]!=row[0]):
				if(pre!=row[1]):
					writer.writerow(["merev_id","yourev_id","mebus_id","youbus_id","topscore"])
				pre=row[1]
				rdic=collections.Counter(row[2:])
				rlen=numpy.linalg.norm(rdic.values())
				#print "rlen",rlen,rdic
				score=0
				for t in idic&rdic:
					score=score+idic[t]*rdic[t]
				if(ilen!=0 and rlen!=0):
					score=score/ilen/rlen
				if(score>max):
					max=score
			l=l+1
			if(l%10000==0):
				print l
	n=n+1
	print n
ifile.close()
wfile.close()
rfile.close()

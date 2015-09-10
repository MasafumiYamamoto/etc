import csv
import numpy
import glob
import os
import time
import collections

#st="NVshopreview"
#st="testin"
st="revsimresult"
revlist=glob.glob(st+"/*")
reflist=glob.glob(st+"/*")

n=0
for revname in revlist:
	print n
	print time.clock()
	if((n%10)==0):
		os.mkdir("simresult/"+str(n/10))
	ifile=open(revname,"r")
	idata=csv.reader(ifile)
	#idata.next()
	for line in idata:
		wfile=open("simresult/"+str(n/10)+"/"+line[0]+".csv","wb")
		#wfile=open("simresult/"+line[0]+".csv","wb")
		writer=csv.writer(wfile)
		writer.writerow(["merev_id","yourev_id","mebus_id","youbus_id","topscore"])
		idic=collections.Counter(line[2:])
		ilen=numpy.linalg.norm(idic.values())
		for refname in reflist:
			max=0
			rfile=open(refname,"r")
			rdata=csv.reader(rfile)
			for row in rdata:
				if(line[0]!=row[0]):
					rdic=collections.Counter(row[2:])
					rlen=numpy.linalg.norm(rdic.values())
#					print "rlen",rlen,rdic
					score=0
					for t in idic&rdic:
						score=score+idic[t]*rdic[t]
					if(ilen!=0 and rlen!=0):
						score=score/ilen/rlen
					if(score>max):
						max=score
			#print time.clock()
			writer.writerow([line[0],row[0],line[1],row[1],max])
			
	n=n+1
				
ifile.close()
wfile.close()
rfile.close()

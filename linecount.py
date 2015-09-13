import csv
import numpy
import glob
import os
import time

st="NVshopreview"
#st="testin"
revlist=glob.glob(st+"/*")
reflist=glob.glob(st+"/*")

time.ctime()
n=0
l=0
for revname in revlist:
	print n
	print revname
	ifile=open(revname,"r")
	idata=csv.reader(ifile)
	wfile=open("revsimresult/"+str(n)+".csv","wb")
	writer=csv.writer(wfile)
	for line in idata:
		l=l+1
	n=n+1
	ifile.close()

print l

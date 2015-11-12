import numpy
import csv
from sklearn.cluster import KMeans
import collections
import glob
import os
import numpy

pas="D:/Lresult/NV_s5/b6t500_LSI_business/"
os.mkdir(pas[:-1]+"_p")

folder=glob.glob(pas+"*")
for infile in folder:
	ifile=open(infile)
	idata=csv.reader(ifile)
	revlist=collections.Counter()
	star=collections.Counter()
	busname=""
	revnum=0
	for line in idata:
		busname=line[2]
		if(line[3]=="4" or line[3]=="5"):
			vec=map(float,line[5:])
			veclen=numpy.linalg.norm(vec)
			if(veclen!=0):
				revlist[line[0]]=vec/veclen
			else:
				revlist[line[0]]=vec
			star[line[0]]=line[3]
			revnum=revnum+1
	ifile.close()
	if(revnum>10):
		kdata=numpy.array(revlist.values())
		kmeans_model=KMeans(n_clusters=10,random_state=1).fit(kdata)
		labels=kmeans_model.labels_

		label=collections.Counter()
		for num in range(0,len(revlist)):
			label[revlist.keys()[num]]=labels[num]

		wfile=open("D:/Lresult/NV_s5/b6t500_LSI_business_p/"+busname+".csv","wb")
		writer=csv.writer(wfile)
		rfile=open(infile,"r")
		rdata=csv.reader(rfile)
		for line in rdata:
			if(line[0] in revlist):
				doc=line[:5]
				doc.append(label[line[0]])
				writer.writerow(doc)
		wfile.close()
		rfile.close()

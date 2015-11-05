import csv
import collections
import numpy
import textedit
import time
import os

print "dim"
dim=raw_input()
pas="D:/Lresult/w2v/"

#####load stopword
stopfile=open("D:/Lresult/stopwords/over4word.csv","r")
stopdata=csv.reader(stopfile)
stoplist=collections.Counter()
for line in stopdata:
	stoplist[line[0]]=1
stopfile.close()
stopfile=open("D:/Lresult/stopwords/b6list.csv","r")
stopdata=csv.reader(stopfile)
for line in stopdata:
	stoplist[line[0]]=1
stopfile.close()
print "stop fin",len(stoplist),time.ctime()

####load vecfile
dfile=open(pas+"scmodoki"+str(dim)+"_5.csv","r")
ddata=csv.reader(dfile)
ddic=collections.Counter()
for line in ddata:
	ddic[line[0]]=map(float,line[1:])
dfile.close()
print "dic fin",len(ddic),len(ddic["we"]),time.ctime()

##base data
revfile=open("D:/Lresult/NV_s5/subrev_1000.csv","r")
revdata=csv.reader(revfile)
revdata.next()
revid=collections.Counter()
revvec=collections.Counter()
for line in revdata:
	revid[line[0]]=line[2]##bus_id
	text=textedit.textedit(line[5])
	revvec[line[0]]=numpy.array([0]*int(dim))
	for num in range(0,len(text)):
		if(num not in stoplist):
			revvec[line[0]]=revvec[line[0]]+numpy.array(ddic[text[num]])
revfile.close()
print "rev fin",len(revvec),time.ctime()

####comp data
sfile=open("D:/Lresult/NVreview.csv","r")
sdata=csv.reader(sfile)
sdata.next()
svec=collections.Counter()
lnum=0
slist=[]
for line in sdata:
	if(line[0] not in revid):
		if(line[2] not in slist):
			slist.append(line[2])
			svec[line[2]]=numpy.array([0]*int(dim))
			doc=textedit.textedit(line[5])
			text=doc.lower().split()
			for num in range(0,len(text)):
				if(num not in stoplist):
					svec[line[2]]=svec[line[2]]+numpy.array(ddic[text[num]])
		else:
			doc=textedit.textedit(line[5])
			text=doc.lower().split()
			for num in range(0,len(text)):
				if(num not in stoplist):
					svec[line[2]]=svec[line[2]]+numpy.array(ddic[text[num]])
	if(lnum%100000==0):
		print lnum,time.ctime()
	lnum=lnum+1
sfile.close()
print "base din",len(svec),time.ctime()

###calc sim svec and revvec
os.mkdir(pas+"NVs5lres_o4b6t"+str(dim))
for rid in revid:
	wfile=open(pas+"NVs5lres_o4b6t"+str(dim)+"/"+rid+".csv","wb")
	writer=csv.writer(wfile)
	writer.writerow(["revid","busid","sim","seikai"])
	rlen=numpy.linalg.norm(revvec[rid])
	if(rlen!=0):
		for sid in svec:
			slen=numpy.linalg.norm(svec[sid])
			if(slen!=0):
				sim=numpy.dot(revvec[rid],svec[sid])/slen/rlen
				writer.writerow([rid,sid,sim,revid[rid]])
			else:
				writer.writerow([rid,sid,0,revid[rid]])
	wfile.close()

print "fin",time.ctime()

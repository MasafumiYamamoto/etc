import csv
import glob
import collections
import numpy
import time
import textedit

pas="D:/Lresult/"
tnum=100

###load stopwords
sfile=open(pas+"stopwords/b6list.csv","r")
stoplist=collections.Counter()
sdata=csv.reader(sfile)
for line in sdata:
    stoplist[line[0]]=1
sfile=open(pas+"stopwords/over4word.csv","r")
sdata=csv.reader(sfile)
for line in sdata:
    stoplist[line[0]]=1
sfile.close()
print "stop fin",time.ctime(),len(stoplist)

###ake subrev list,line[2]==seikai
subfile=open(pas+"NV_s5/subrev_1000.csv","r")
subdata=csv.reader(subfile)
subdata.next()
subidlist=collections.Counter()
for line in subdata:
    subidlist[line[0]]=line[2]
subfile.close()
print "sub fin",len(subidlist)

###load buslist
busfile=open(pas+"NVshoplist.csv","r")
busdata=csv.reader(busfile)
busdata.next()
busidlist=collections.Counter()
for line in busdata:
    busidlist[line[0]]=1
busfile.close()
print "bus fin",len(busidlist)

###laod train bow
bbowlist=collections.Counter()
bbowlen=collections.Counter()
for bus in busidlist:
    busname=bus
    bbowlist[busname]=collections.Counter()
    bfile=open(pas+"NVbusbow/"+bus+".csv","r")
    bdata=csv.reader(bfile)
    bdata.next()
    for line in bdata:
        if(line[0] not in stoplist):
            bbowlist[busname][line[0]]=int(line[1])
    le=0
    for t in bbowlist[busname]:
        le=le+bbowlist[busname][t]*bbowlist[busname][t]
    bbowlen[busname]=numpy.sqrt(le)
    bfile.close()
print "train fin",len(bbowlist),time.ctime()
#print bblen

snum=0
###load subrev bow
for sub in subidlist:
    subfile=open(pas+"NV_s5/subrevbow/"+sub+".csv","r")
    subdata=csv.reader(subfile)
    subdata.next()
    snum=snum+1
    if(snum%100==0):
        print snum,time.ctime()
    sublist=collections.Counter()
    for line in subdata:
        if(line[0] not in stoplist):
            sublist[line[0]]=int(line[1])
    le=0
    for t in sublist:
        le=le+sublist[t]*sublist[t]
    sublen=numpy.sqrt(le)
    wfile=open(pas+"bowo4b6/resnrnto4b6/"+sub+".csv","wb")
    writer=csv.writer(wfile)
    writer.writerow(["revid","busid","score","seikai"])
    for bus in busidlist:
        score=0
        if(bbowlen[bus]*sublen!=0):
            for t in sublist:
                if(t in bbowlist[bus]):
                    score=score+bbowlist[bus][t]*sublist[t]
            score=score/bbowlen[bus]/sublen
      #  print line[0],bus,score,sublen,bblen[bus]
        writer.writerow([sub,bus,score,subidlist[sub]])
    wfile.close()

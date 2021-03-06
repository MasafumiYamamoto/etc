import csv
import glob
import collections
import numpy
import time

pas="D:/Lresult/"
tnum=100

###ake subrev list
subfile=open("subrev_1000.csv","r")
subdata=csv.reader(subfile)
subdata.next()
subidlist=collections.Counter()
for line in subdata:
    subidlist[line[0]]=line[1]
subfile.close()

###load tsopfile
stopfile=open("stopwords/b6list.csv","r")
stopdata=csv.reader(stopfile)
stoplist=collections.Counter()
for line in stopdata:
    stoplist[line[0]]=1
stopfile.close()

####load w2v list
w2vfile=open("w2v/scmodoki"+str(tnum)+"_5.csv")
w2vdata=csv.reader(w2vfile)
w2vdic=collections.Counter()
for line in w2vdata:
    w2vdic[line[0].lower()]=map(float,line[1:])
w2vfile.close()
print "w2v fin",len(w2vdic),time.ctime()

###laod train bow
busbowlist=glob.glob("NVbus_o4_bow/*")
bblist=collections.Counter()
for bus in busbowlist:
    busname=bus[13:-4]###bus_id####
    bblist[busname]=collections.Counter()
    bfile=open(bus,"r")
    bdata=csv.reader(bfile,delimiter="\t")
    for line in bdata:
        if(line[1] not in stoplist):
            bblist[busname][line[1]]=int(line[2])
    bfile.close()
print "train fin",len(bblist),time.ctime()

###load subrev bow
subbowlist=glob.glob("NVsub_o4_bow/*")
snum=0
for subrev in subbowlist:
    print subrev,time.ctime()
    snum=snum+1
    ifile=open(subrev,"r")
    idata=csv.reader(ifile,delimiter="\t")
    revname=subrev[13:-4]
    print revname,time.ctime(),snum
    wfile=open(revname+".csv","wb")
    writer=csv.writer(wfile)
    writer.writerow(["revid","busid","sim","seikai"])
    sblist=collections.Counter()####bow dic
    for line in idata:
        if(line[1] not in stoplist):
            sblist[line[1]]=int(line[2])
    ifile.close()
    bnum=0
    sblen=numpy.linalg.norm(sblist.values())
    for bus in bblist:
        bnum=bnum+1
        score=0
        if(sblen!=0):
            for t in sblist:
                if(t in w2vdic):
                    tvec=w2vdic[t]
                    minw=""
                    mind=10000
                    match=0
                    bblen=numpy.linalg.norm(bblist[bus].values())
                    if(bblen!=0):
                        for w in bblist[bus]:
                            if(t==w):
                                match=1
                            wvec=w2vdic[w]
                            d=numpy.linalg.norm(numpy.array(tvec)-numpy.array(wvec))
                            if(d<mind):
                                minw=w
                                mind=d
                        if(mind<1):
                            if(match==1):
                                minw=t
                            score=score+sblist[t]*bblist[bus][minw]
                else:
                    if(t in bblist[bus]):
                        score=score+sblist[t]*bblist[bus][t]
        if(sblen!=0 and bblen!=0):
            score=score/sblen/bblen
        writer.writerow([revname,bus,score,subidlist[revname]])
    ifile.close()
    wfile.close()

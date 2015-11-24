import csv
import collections

cfile=open("D:/Lresult/ks/busclus/4bEjOyTaDG24SY5TxsaUNQ_clusp.csv","r")
cdata=csv.reader(cfile)
idlist=collections.Counter()
cdata.next()
for line in cdata:
    idlist[line[0],line[1]]=line[2]

wfile=open("D:/Lresult/ks/busent_cw/4bEjOyTaDG24SY5TxsaUNQ.csv","wb")
writer=csv.writer(wfile)
writer.writerow(["revid","userid","busid","star","date","anv","sent","raw","clus"])

cfile=open("D:/Lresult/ks/busent_anv/4bEjOyTaDG24SY5TxsaUNQ_cw.csv","r")
cdata=csv.reader(cfile)
for line in cdata:
    wlist=[]
    if((line[0],line[6]) in idlist):
        wlist=line+[idlist[line[0],line[6]]]
    else:
        wlist=line+["_"]
    writer.writerow(wlist)

cfile.close()
wfile.close()

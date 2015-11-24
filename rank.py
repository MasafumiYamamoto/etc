#for rev_shop
###b describe ignore score out

import csv
import glob
import time

def main(pas_,dim_,w_):
	pas="D:/Lresult/w2v/wbs"
	dim=str(dim_)
	w=float(w_)
	ww=str(w_)[2:]
	####output file
	revlist=glob.glob(pas+"/wbs_d"+str(dim)+"/*")
	for w in [0.2,0.4,0.6,0.8,1.0,0.5]:
		print w,"start",time.ctime()
		ww=str(w)[2:]
		wfile=open(pas+"/ranking/wbs_d"+str(dim)+"w"+str(ww)+".csv","wb")
		#wfile=open(pas+"/ranking/c500d100/wbs_c500d100w"+str(ww)+".csv","wb")
		wri=csv.writer(wfile)
		wri.writerow(["revid","mybus","ranking","topscore","topbus","myscore"])
		l=0
		for review in revlist:
			ifile=open(review,"r")
			idata=csv.reader(ifile)
			idata.next()
			seikai=0
			top=-1
			tbus=""
			mybus=""
			revid=""
			for line in idata:
				if(line[1]==line[4]):###make seikai
					seikai=w*float(line[2])+(1-w)*float(line[3])
					mybus=line[4]
					revid=line[0]
				if(top<w*float(line[2])+(1-w)*float(line[3])):
					top=w*float(line[2])+(1-w)*float(line[3])
					tbus=line[1]
			ifile=open(review,"r")
			idata=csv.reader(ifile)
			idata.next()
			rank=1
			for line in idata:
				if(seikai<w*float(line[2])+(1-w)*float(line[3])):
					rank=rank+1
			wri.writerow([revid,mybus,rank,top,tbus,seikai])
			l=l+1
			if(l%100==0):
				print l,time.ctime()
			ifile.close()
		wfile.close()


if __name__ == '__main__':
	print "pas"
	pas=raw_input()
	print "dim"
	dim=raw_input()
	print "w"
	w=raw_input()
	main(pas,dim,w)

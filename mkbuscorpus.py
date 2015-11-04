def main(model_,bnum_,tnum_,train_,pas_):
	from gensim import corpora, models, similarities
	import csv
	import textedit
	import time
	import glob

	model=str(model_)
	bnum=int(bnum_)
	tnum=int(tnum_)
	train=str(train_)
	pas=str(pas_)

	print "mkcorpus_start",time.ctime()
	#remove subrev
	subfile=open(pas+"subrev_1000.csv","r")
	subdata=csv.reader(subfile)
	sublist=[]
	for line in subdata:
		sublist.append(line[0])
	subfile.close()

	##remove stoplist
	stopfile=open(pas+"stopwords/over4word.csv","r")
	stopdata=csv.reader(stopfile)
	stoplist=[]
	for line in stopdata:
		stoplist.append(line[0])
	stopfile.close()
	stopset=set(stoplist)

	##make documents
	st="D:/Lresult/NVbus/*"
	dlist=glob.glob(st)
	print len(dlist),"star"
	dnum=0
	for bus in dlist:
		dfile=open(bus,"r")
		ddata=csv.reader(dfile)
		dlist=[]
		for line in ddata:
			if(line[0] not in sublist):
				te=line[5]
				doc=textedit.textedit(te)
				dlist.append(doc)
				dnum=dnum+1
				if(dnum%1000==0):
					print dnum,
		dfile.close()

		texts = [[word for word in document.lower().split()] for document in dlist]
		#print "text fin",time.ctime(),texts
		texts = [[word for word in text if word not in stopset] for text in texts]

		dictionary = corpora.Dictionary(texts)
		#print "dictionary fin",time.ctime(),len(dictionary.token2id)
		#dictionary.filter_extremes(no_below=bnum)
		#print "dictionary cut fin",time.ctime(),len(dictionary.token2id)

		#dictionary.save(pas+train+"_o4b"+str(bnum)+"t"+str(tnum)+".dict")
		dictionary.save_as_text(pas+"NVbus_o4b6_bow/"+bus[17:-4]+".tsv")

		#corpus=[dictionary.doc2bow(text) for text in texts]
		#corpora.MmCorpus.serialize(pas+train+"_o4b"+str(bnum)+".mm", corpus)
		#print "mk_corpus fin",time.ctime()


if __name__ == '__main__':
	#print "model"
	#model_=raw_input()
	model_=0
	#print "bnum"
	bnum_=6
	#print "tnum"
	tnum_=10
	#print "train"
	#train_=raw_input()
	train_="NVreview"
	#print "pas"
	pas_="D:/Lresult/"
	main(model_,bnum_,tnum_,train_,pas_)

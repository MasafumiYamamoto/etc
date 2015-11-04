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
	##remove stoplist
	stopfile=open(pas+"stopwords/over4word.csv","r")
	stopdata=csv.reader(stopfile)
	stoplist=[]
	for line in stopdata:
		stoplist.append(line[0])
	stopfile.close()
	stopset=set(stoplist)

	##make documents
	dnum=0
	subfile=open(pas+"subrev_1000.csv","r")
	subdata=csv.reader(subfile)
	subdata.next()
	for line in subdata:
		dlist=[]
		te=line[2]
		doc=textedit.textedit(te)
		dlist.append(doc)
		dnum=dnum+1
		if(dnum%100==0):
			print dnum,
		texts = [[word for word in document.lower().split()] for document in dlist]
		texts = [[word for word in text if word not in stopset] for text in texts]
		dictionary = corpora.Dictionary(texts)
		dictionary.save_as_text(pas+"NVsub_o4_bow/"+line[0]+".tsv")
	subfile.close()


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

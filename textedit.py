def textedit(text):
	te=text.lower()
	te=te.replace("!"," ")
	te=te.replace('"'," ")
	te=te.replace("#"," ")
	te=te.replace("$"," ")
	te=te.replace("%"," ")
	te=te.replace("&"," ")
	te=te.replace("'"," ")
	te=te.replace("("," ")
	te=te.replace(")"," ")
	te=te.replace("="," ")
	te=te.replace("-"," ")
	te=te.replace("^"," ")
	te=te.replace("~"," ")
	te=te.replace("|"," ")
	
	te=te.replace("["," ")
	te=te.replace("]"," ")
	te=te.replace("{"," ")
	te=te.replace("}"," ")
	te=te.replace("`"," ")
	te=te.replace("@"," ")
	te=te.replace("+"," ")
	te=te.replace(";"," ")
	te=te.replace("*"," ")
	te=te.replace(":"," ")
	te=te.replace("<"," ")
	te=te.replace(","," ")
	te=te.replace(">"," ")
	te=te.replace("."," ")
	te=te.replace("?"," ")
	te=te.replace("/"," ")
	te=te.replace("_"," ")
	
	return te
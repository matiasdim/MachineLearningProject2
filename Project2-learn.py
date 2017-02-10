#reading data
file  = open("forumTraining-stemmed", "r") 

#geting documents and vocabulary of each one
documents = file.readlines()
vocabulary = [] #array containing vocabulary for each document
categories = {} # Hash too store each category and its number of apparences in ALL documents
category_prob = {} # hash with each document's categories and probability
text_j = {} # hash with category as key and the value is all docs for that category
prob_w_c = {}
for d in documents:
	document_vocabulary = [] # array containing vocabulary for thecurrent document

	document_words = d.split()
	category = document_words.pop(0)
	# getting categories of the dataset and number of category apparences per document
	if not (category in categories):		
		categories[category] = 1.0		
	else:
		categories[category] = categories[category] + 1.0
	

	# getting vocabulary for current document	
	for dc in document_words:
		if text_j.has_key(category):
			text_j[category] += [dc]
		else:
			text_j[category] = [dc]
		if not (dc in document_vocabulary):
			document_vocabulary.append(dc)

	vocabulary+= document_vocabulary

vocabulary = set(vocabulary)

# !!!! Probability estimate of a particular class: P(cj) = |Docsj| / |training documents|
for k in categories:
	category_prob[k] = categories[k] / len(documents)
	print category_prob[k]

# Getting n_k
def get_nk(word, text):
	word_count = 0
	for text_word in text:
		if word == text_word:
			word_count += 1
	return word_count

prob_w_c = {} # {category:{'word':prob}} 
for k,v in text_j.iteritems():	
	n_k = -1 # {word = number_of_Aparrences} nk = number of times wk occurs in Textj
	prob_w_c[k] = {}
	for word in vocabulary:
		n_k = get_nk(word,v)		
		prob_w_c[k][word] = (n_k + 1.0) / (len(set(v)) + len(vocabulary))# P(wk | cj) = (nk + 1) / (n + |Vocabulary|)
		print str(prob_w_c[k])
	


#











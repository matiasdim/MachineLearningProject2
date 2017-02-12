import cPickle as pickle
import math

fileObject = open("c_probabilities",'r')  
c_prob = pickle.load(fileObject)  # structure containing P(Cj) # {category:prob}

fileObject_2 = open("w_c_probabilities",'r')  
w_c_prob = pickle.load(fileObject_2)  # structure containing P(wk | cj) format: # {category:{'word':prob}} 

fileObject_3 = open("categories",'r')  
categories = pickle.load(fileObject_3)  # structure containing categories

fileObject_4 = open("vocabulary",'r')  
vocabulary = pickle.load(fileObject_4)  # structure containing vocabulary

#reading test data
file  = open("forumTest-stemmed", "r") 

#geting documents and vocabulary of each one
documents = file.readlines()

documents_categories = [] #
document_calculated_cat = {}
category_result = {} 
for d in documents:
	print d
	for c in categories:
		productory = 0.0
		document_words = d.split()
		document_words = document_words.pop(0)
		for word in document_words:
			if word in vocabulary:
				pw = w_c_prob[c][word] # hash P(Wk | Cj)
				productory += math.log(pw)
		p_c = c_prob[c] # hash P(Cj)		
		prod = math.exp(productory)
		category_result[c] = p_c * prod		
	max(category_result)

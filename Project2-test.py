import cPickle as pickle

fileObject = open("c_probabilities",'r')  
c_prob = pickle.load(fileObject)  # structure containing P(Cj)

fileObject_2 = open("w_c_probabilities",'r')  
w_c_prob = pickle.load(fileObject)  # structure containing P(wk | cj)

fileObject_2 = open("categories",'r')  
categories = pickle.load(fileObject)  # structure containing categories

fileObject_2 = open("vocabulary",'r')  
vocabulary = pickle.load(fileObject)  # structure containing vocabulary

#reading test data
file  = open("forumTest-stemmed", "r") 

#geting documents and vocabulary of each one
documents = file.readlines()

positions = [] # array with all word positions in every Document containing tokens in Vocabulary

for d in documents:

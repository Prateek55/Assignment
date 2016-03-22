# Find all concepts whose polarity is different for NLTK and senticNet
#The same file is modified for both +ve and -ve by replacing pos <-> neg
import nltk.sentiment.vader as sentiment
sn=sentiment.SentimentIntensityAnalyzer() # Sentiment Analyser for NLTK
neg_corpus=[]

# Stores all the pos/neg concepts in SenticNet and store in an array
with open("neg_word_corpus") as neg_corpus_file:
	for line in neg_corpus_file:
		word=line[:-1]
		neg_corpus.append(word)

collision_file=open('colliding_polarity','w') # The file has been renamed to nltk_collisions_N/P

for term in neg_corpus:
	nltk_polarity=sn.polarity_scores(term)
	if nltk_polarity['pos']>nltk_polarity['neg']: # have opposite polarity
		print nltk_polarity
		collision_file.write(term+"<-P\n") # store the result


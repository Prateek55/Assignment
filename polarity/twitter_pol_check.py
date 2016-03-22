# Identify concepts from the new set of words from Twitter which have opposite polarity
# The same file is edited for both pos and neg concepts, changing pos to neg and positive to negative
pos_corpus=[]

with open("../data/pos_word_corpus") as pos_corpus_file: # SenticNet positive polarity concepts
	for line in pos_corpus_file:
		word=line[:-1]
		pos_corpus.append(word)
collision_file=open("../collisions/tweet_collision","w") # the File has been renamed now

with open('../data/negative-words.txt') as tweet_neg_corpus: # New Twitter data set, came classified as positive and negative beforehand
	for line in tweet_neg_corpus:
		term=line[:-1]
		if term in pos_corpus:
			collision_file.write(term+" <- N\n")
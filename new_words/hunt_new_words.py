pos_corpus=[]
neg_corpus=[]
new_neg_file=open("negative","w")
with open("../data/pos_word_corpus") as pos_corpus_file:
	for line in pos_corpus_file:
		word=line[:-1]
		pos_corpus.append(word)
with open("../data/neg_word_corpus") as neg_corpus_file:
	for line in neg_corpus_file:
		word=line[:-1]
		neg_corpus.append(word)

with open("../data/negative-words.txt") as new_concept:
	for line in new_concept:
		concept=line[:-1]
		if concept not in neg_corpus and concept not in pos_corpus:
			new_neg_file.write(concept+"\n")
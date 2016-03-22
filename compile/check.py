neg_corpus=[]
with open("../data/neg_word_corpus") as neg_file:
	for line in neg_file:
		line = line[:-1]
		neg_corpus.append(line)

with open ("reviewed_neg_concepts") as concepts:
	for concept in concepts:
		word=concept.split("=")[0]
		if word in neg_corpus:
			print word
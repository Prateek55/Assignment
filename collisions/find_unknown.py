pos_corpus=[]
neg_corpus=[]
unknown_file=open("unknown","w")

# Function check_pos/neg checks the presence of a neg/pos polarity word in semantics
# Return 1 if present, else 0
def check_pos(semantics):
	err=0
	for word in semantics:
		if word in pos_corpus:
			err_file.write("#"+word+"<- P | ")
			err=1
			break
	return err

def check_neg(semantics):
	err=0
	for word in semantics:
		if word in neg_corpus:
			err=1
			err_file.write("#"+word+"<- N | ")
			break
	return err

#Stores all pos/neg concepts of SenticNet in pos/neg_data_corpus
with open("pos_word_corpus") as pos_corpus_file:
	for line in pos_corpus_file:
		word=line[:-1]
		pos_corpus.append(word)
with open("neg_word_corpus") as neg_corpus_file:
	for line in neg_corpus_file:
		word=line[:-1]
		neg_corpus.append(word)
i=0


with open("semantic_map") as sem_map:
	for line in sem_map:
		i+=1
		line=line[:-1]
		concept=line.split("#")[0]
		semantics=line.split("#")[1:5]
		err=0
		for term in semantics:
			# Check whether term is present in negative or positive concept
			if term not in pos_corpus and (term not in neg_corpus):
				err=1
				unknown_file.write(term+" ")
				break

		if err==1: # Print the ones absent in both
			unknown_file.write("<- "+concept+"\n")

				
			

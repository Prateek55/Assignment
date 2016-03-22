pos_corpus=[]
neg_corpus=[]
err_file=open("../collisions/error","w")

# Function check_pos/neg checks the presence of a neg/pos polarity word in semantics
# Return 1 if present, else 0
def check_pos(semantics):
	err=0
	for word in semantics:
		if word in pos_corpus:
			err_file.write("#"+word+"<- P | ")
			err=1
	return err

def check_neg(semantics):
	err=0
	for word in semantics:
		if word in neg_corpus:
			err=1
			err_file.write("#"+word+"<- N | ")
	return err

#Stores all pos/neg concepts of SenticNet in pos/neg_data_corpus
with open("../data/pos_word_corpus") as pos_corpus_file:
	for line in pos_corpus_file:
		word=line[:-1]
		pos_corpus.append(word)
with open("../data/neg_word_corpus") as neg_corpus_file:
	for line in neg_corpus_file:
		word=line[:-1]
		neg_corpus.append(word)
i=0

# Loop over each concept 
with open("../data/semantic_map") as sem_map:
	for line in sem_map:
		i+=1
		line=line[:-1]
		concept=line.split("#")[0]
		semantics=line.split("#")[1:5] # Semanics for the concept stored
		err=0;
		unknown=0;
		print i,concept
		# Check the presence of problematic concepts
		if concept in pos_corpus:
			err=check_neg(semantics)
		else:
			err=check_pos(semantics)
		if err==0:
			continue;
		elif err==1:
			err_file.write(concept+"\n") #Stores problematic concepts in error file
				
			

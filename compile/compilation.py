# The file picks up the result of moods and semantics for new tweeter words
# The same file is modified for both positive and negative words exchanging pos<->neg and positive<->nnegative
concepts={}


##importing moods
with open('../moods/neg_moody_words','r') as mood_file:
	for line in mood_file:
		line=line[:-1]
		splits=line.split(" ")
		print splits[0]
		concepts[splits[0]]=["#"+splits[1],"#"+splits[2]]
		# Create a dictionary of Concept vs moods that were stored after computation


with open('../semantics/neg_semantics') as semantic_file: # Where Semantics were stored
	for line in semantic_file:
		line =line[:-1]
		semantics=line.split("#")
		for i in range(1,6):
			concepts[semantics[0]].append(semantics[i])
		# Append semantics to the above dictionary

concept_file=open('neg_concepts','w') # Writing concept to file
for concept,attributes in concepts.iteritems():
	toWrite=concept+"=["
	for term in attributes:
		toWrite+=term+","
	toWrite=toWrite[:-1]+"]\n"
	concept_file.write(toWrite)

neg_sem_map={}
neg_word_corpus=[]

# Create a dictionary of concept vs semantic from sematic map
with open('../data/semantic_map') as sem_map:
	for line in sem_map:
		line = line[:-1]
		splits=line.split("#")
		if float(splits[-1])<0.0:
			neg_word_corpus.append(splits[0])
			neg_sem_map[splits[0]]=splits[1:-1]

error_map={}
# Creare a dictionary of all problematic concepts
# The dictionary contain all opposite polarity semantics for each concept
with open('../collisions/error_log') as error_file:
	for line in error_file:
		line=line[:-1]
		line=line.replace("#","")
		if "__P__" not in line:
			continue
		concept=line.split("__P__")[-1]
		error_map[concept]=(line.split("__P__"))[:-1]

sugg_map={}
# Picks up similar semantics computer in pos/neg_correction.py 
# Create a map of problematic concept vs new semantics
with open("../collisions/new_semantic/neg_correction") as sugg_sem_file:
	for line in sugg_sem_file:
		line=line[:-1]
		concept=line.split("#")[0]
		poss_sugg=line.split("#")[1:]
		sugg_map[concept]=[]
		count=len(error_map[concept])
		i=0
		for sugg in poss_sugg:
		 	if i>=count:
		 		break
		 	if sugg not in neg_sem_map[concept] and sugg!=concept:
		 		i+=1
		 		sugg_map[concept].append(sugg)
		toWrite=concept+"="+str(sugg_map[concept])+" in place of "+str(error_map[concept])
		print toWrite

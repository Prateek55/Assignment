The file structure for the directory is as follows:

There are multiple directories:

	1. data: Contain files have list of all the concepts with positive or negative polarity
		i.   data.xml : Sentic 3.0 XML file but with slight tag renaming for easy reading
		ii.  negative-words.txt/positve-words.txt : Contain a new set of words with negative/positive polarity downloaded from https://github.com/jeffreybreen/twitter-sentiment-analysis-tutorial-201107/blob/master/data/opinion-lexicon-English/
		iii. semantic_map : All concepts mentioned in the XML file are stored in the following format: 
			concept#semantic1#semantic2#semantic3#semantic4#semantic5#polarity
			The file is used for fast extraction of data.
		iv.  neg/pos/neut_word_corpus: Stores list of all concepts with positive/negative/neutral polarity that are present in SenticNet.

	2. moods: Contain files that both compute the concept-related moods as well as store the concepts in different files depending on positive or negative polarity.
		i.  find_(pos/neg)_mood.py : The file extracts all the NEW concepts of pos/neg polarity and allocate mood based on similarity score from related moods. It then stores them in the following files.
		ii.  neg/pos_moody_words.py : The file contains list of all the concepts for which appropriate distinct score was generated in the following format 
			concept mood1 mood2
		iii. neg/pos_moody_words.py: Same as above but store similarity score as well.

	3. new_words: Contains files for extracting new words as well as storing them.
		i.  hunt_new_words.py: From the new set of words, it extract words not present in SenticNet.
		ii. negative/positive: List of new pos/neg concepts not present in SenticNet

	4. polarity: Contain files that deal with polarity calculation
		i.   nltk_pol_calc.py : sample code for polarity calculation using nltk
		ii.  polarity_classifier.py : create the files neg/pos/neut_corpus in data folder by classifying on the basis of polarity given in SenticNet.
		iii. twitter_pol_check : Find the words that have different polarities in new Twitter data and SenticNet. Store them in a file in collision folder
		iv.  find_pol_er.py : find all the concepts of SenticNet that have opposite polarities of semantics.

	5. semantics : Contain files responsible for computing related semantics of the new concepts. The semantics are picked up from the concepts of SenticNet itself.
		i.  pos/neg_semantics : Store 10 most closely related semantics for new concepts for which appropriate mood could be generated.
		ii. find_sem.py : Generate the above file.

	6. compile : Contain file responsible for combining moods and semantics of the new words and storing them in appropriate file.
		i.   neg/pos_concepts: Contain the new concepts in the appropraite format
		ii.  reviewed_neg/pos_concepts : The above file, after manual inspection for verb inflections/plurals and removing inappropriate concepts.
		iii. compilation.py: Create the above file by combining moods and semantics from their files in the moods and semantics directory

	7. collisions: Contains all the concepts with opposite polarities in different lexicons. Also include the file that generate new sementics for the concepts with problematic concepts.
		i.   collision_polarity_finder.py : Find all the stored concepts that have opposite polarities in SenticNet and NLTK and stores them.
		ii.  find_pol_er.py : Find all concepts which have problematic semantics, i.e. opposite polarity and stores them in error files
		iii. error/error_log : Store problematic concepts in different format.
		iv.  find_unknow.py : Find all semantics and there corresponding concepts where semantic is not itself a concept in SenticNet.
		v.   pos/neg_correction.py : For all possible problematic concepts, the file find appropraite list of semantics from SenticNet. 
		vi.  suggest_semantics.py : Find the appropriate semantics from the above result that can act as substitution for problematic substitution.

		vii. nltk_collision_N/P : Concepts with opposite polarities in nltk and senticNet. The format is "Concept <- P" if the concept is positive in SenticNet and negative in NLTk. "Concept<-N" is for vice-verse.
		viii.tweet_collision_N/P: Similar as above, just for the new data.

		ix. reviewed/reviewed_nltk_coll_N/P: Same as above file, but after reviewing the concepts manually. 
		x.  reviewed/reviewed_tweeter_coll_N/P: Same as above file, but after reviewing the concepts manually.

		xi. pos/neg_correction : Contain the list of similar semantics from SenticNet for problematic concepts
		xii.suggested_semantics : Contains the suggested semantics for problematic concepts.





    # -*- coding: utf-8 -*-
    """
    Created on Thu Jan 31 17:12:34 2019
    
    @author: zeugn
    """
    
    import nltk
    import os
    from nltk import FreqDist
    import re
    from nltk.collocations import*
    
    os.getcwd()
    os.chdir('C:\\Users\zeugn\Documents')
       
    #read text file in - state of the union part2
    file = open('sotupart2.txt', 'r')
    speech = file.read()
    
    #convert the text into strings
    Token = nltk.word_tokenize(speech)
    Token[:50]
    words = [w.lower() for w in Token]
    len(words)
    
    vocab = sorted(set(words))
    print(vocab)
    
    def alpha_filter(w):
        pattern = re.compile('^[^a-z]+$')
        if (pattern.match(w)):
            return True
        else:
            return False
    
    alphatokens = [w for w in words if not alpha_filter(w)]
    
    #Implement stopwords and delete them to get better insights
    nltkstopwords = nltk.corpus.stopwords.words('english')
    otherstopwords = ['could','would','might','must','need', 'sha','wo','y', "'s", "'d", "'ll", "'t", "'re" ]
    
    stopwords = nltkstopwords + otherstopwords
    
    stoppedtokens = [w for w in alphatokens if not w in stopwords]
    print(stoppedtokens[:50])
    
    
    #Frequency distribution with the stopped word
    fdist = FreqDist(stoppedtokens)
    fdistkeys = list(fdist.keys())
     
    topkeys = fdist.most_common(50)
    
    for pair in topkeys:
        print(pair)
        
    numwords = len(Token)
    topkeys_normalized = [(word,(freq/numwords) * 100) for (word,freq) in topkeys]
    
    for pair in topkeys_normalized:
        print(pair)
        
    bigrams = list(nltk.bigrams(stoppedtokens))
    
    bigram_measures = nltk.collocations.BigramAssocMeasures()
        
    finder = BigramCollocationFinder.from_words(stoppedtokens)
    scored = finder.score_ngrams(bigram_measures.raw_freq)
    
    for bscore in scored[:50]:
        print(bscore)
        
        
    
    #Mutual Information Score
    
    finder2 = BigramCollocationFinder.from_words(stoppedtokens)
    finder2.apply_freq_filter(5)
    scored2 = finder2.score_ngrams(bigram_measures.pmi)
    for bscore in scored2[:50]:
        print(bscore)
    
    
    
    
        
        
    
    
    
    
    
        
      
    
    
    
    
    
    
    
    
    
    
    

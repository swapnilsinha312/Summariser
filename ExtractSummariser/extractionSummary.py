# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 13:08:46 2021

@author: aj240
"""

#making a summarizer function which given a string as the parameter will return
#a summary string in the end

import numpy as np
import pandas as pd
import nltk
#nltk.download('punkt') # one time execution
import re

def summary(text):
    sentences=text.split(".")
    
    if(len(sentences)<10):
        print('text insufficient')
        return "retry"
    # Extract word vectors
    word_embeddings = {}
    f = open('glove.6B.100d.txt', encoding='utf-8')
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        word_embeddings[word] = coefs
    f.close()
    
    # remove punctuations, numbers and special characters
    clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")

    # make alphabets lowercase
    clean_sentences = [s.lower() for s in clean_sentences]
    
    #removing stopwords
    #nltk.download('stopwords')
    from nltk.corpus import stopwords
    stop_words = stopwords.words('english')

    # function to remove stopwords
    def remove_stopwords(sen):
        sen_new = " ".join([i for i in sen if i not in stop_words])
        return sen_new

    # remove stopwords from the sentences
    clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]
    
    sentence_vectors = []
    for i in clean_sentences:
        if len(i) != 0:
            v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
        else:
            v = np.zeros((100,))
        sentence_vectors.append(v)
   
    # similarity matrix
    sim_mat = np.zeros([len(sentences), len(sentences)])
    from sklearn.metrics.pairwise import cosine_similarity

    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,100), sentence_vectors[j].reshape(1,100))[0,0]
    # importing networkx  
    import networkx as nx 
 
    nx_graph = nx.from_numpy_array(sim_mat)

    #applying the page rank alg
    scores = nx.pagerank(nx_graph)
    
    ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)
    
    final_text = ''
    # Extract top 5 sentences as the summary
    for i in range(5):
        final_text+=(ranked_sentences[i][1]+"\n")
    
    return final_text
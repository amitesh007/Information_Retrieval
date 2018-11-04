from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import nltk
from nltk.stem.porter import PorterStemmer
import os
import docx
import csv

'''
This method is used to get the text file from docx file.
'''
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
    
    
'''
This method is used to get words from a given text
'''
def tokenizer(text):
    tokens = nltk.tokenize.word_tokenize(text)
    return tokens


'''
This method is used to remove the stop word,and process the text with stemmer and lammatizer. 

def with_preprocessing(text):
    tokens = tokenizer(text)
    stemmer = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    lemma = WordNetLemmatizer()
    new_text = ""
    new_text_1 = ""
    for token in tokens:
        token = token.lower()
        if token not in stop_words:
#           Using Stemmer  
            new_text += stemmer.stem(token)
            new_text += " "
    tokens1 = tokenizer(new_text)
    for token in tokens:
        if token not in tokens1:
#           Using Lemmatizer
            new_text_1 += lemma.lemmatize(token)
            new_text_1 += " "
    return new_text_1
'''

'''
This method will get the text without preprocessing it.
'''
def without_preprocessing(text):
    tokens = tokenizer(text)
    new_text = ""
    for token in tokens:
        new_text += token
        new_text += " "
    return new_text


'''
This method is used to get the Inveted Index
'''
def invertedIndex():
    inverted = {}
    list_doc =  [x for x in os.listdir() if x.endswith(".docx")]
    for doc in list_doc:
        doc_loc =  str(doc)
        file_text = getText(doc_loc)
        file_text = without_preprocessing(file_text)
        tokens = tokenizer(file_text)
        for word in tokens:
            if not inverted.__contains__(word):
                count = 1
                doclist = {}
                doclist[doc] = 1
                inverted[word] = doclist
            else:
                if doc in inverted[word]:
                    doclist = inverted[word]
                    doclist[doc] += 1
                    inverted[word] = doclist
                else:
                    count = 1
                    doclist = inverted[word]
                    doclist[doc] = count
                    inverted[word] = doclist
    return inverted

'''
Main Method to get the inverted index and create an ouput cv file for Inverted Index
'''                 
indexed_docs = invertedIndex()

with open('inverted_index_file_without_pre_processing.csv', 'w') as f:
    w = csv.DictWriter(f, indexed_docs.keys())
    w.writeheader()
    w.writerow(indexed_docs)


w = csv.writer(open("inverted_index_formated_file_without_pre_processing.csv", "w"))
for key, val in indexed_docs.items():
    w.writerow([key, val])
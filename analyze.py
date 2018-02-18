#from porter import Porter
import nltk
import re

def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})

def trainAnger():
    #Delete common chars like comma
    regex = re.compile('[\[,\.!?—\]]') 
    pos = []
    with open("./pos_rom.txt") as f:
        for i in f: 
            pos.append([format_sentence(regex.sub('', i.lower())), 'pos'])
    neg = []
    with open("./neg_rom.txt") as f:
        for i in f: 
            neg.append([format_sentence(regex.sub('', i.lower())), 'neg']) 
   # next, split labeled data into the training and test data
    training = pos[:int((.8)*len(pos))] + neg[:int((.8)*len(neg))]
    test = pos[int((.8)*len(pos)):] + neg[int((.8)*len(neg)):]
    from nltk.classify import NaiveBayesClassifier
    classifier = NaiveBayesClassifier.train(training)
    from nltk.classify.util import accuracy
    print("Test data accuracy" + str(accuracy(classifier, test)))
    classifier.show_most_informative_features()
    data=[]
    with open("./raw.txt", 'r', encoding='utf-8') as f:
        data=f.read()
    return classifier
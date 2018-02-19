#from porter import Porter
import nltk
import re

def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})

def trainLove():
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
    #with open("./raw.txt", 'r', encoding='utf-8') as f:
    #    data=f.read()
    return classifier

def trainDanger():
    danger = []
    with open("./anger.txt") as f:
        for i in f: 
            danger.append([format_sentence(i), 'danger'])
    calm = []
    with open("./calm.txt") as f:
        for i in f: 
            calm.append([format_sentence(i), 'calm']) 
    training = danger[:int((.8)*len(danger))] + calm[:int((.8)*len(calm))]
    test = danger[int((.8)*len(danger)):] + calm[int((.8)*len(calm)):]
    from nltk.classify import NaiveBayesClassifier
    classifier = NaiveBayesClassifier.train(training)
    from nltk.classify.util import accuracy
    print("Test data accuracy" + str(accuracy(classifier, test)))
    classifier.show_most_informative_features()
    return classifier
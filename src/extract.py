import nltk
import pprint
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

sents = nltk.corpus.treebank_raw.sents()
tokens = []
boundaries = set()
offset = 0
for sent in sents:
  tokens.extend(sent)
  offset += len(sent)
  boundaries.add(offset-1)

def punct_features(tokens, i):
  return {'next-word-capitalized': tokens[i+1][0].isupper(),
          'prev-word': tokens[i-1].lower(),
          'punct': tokens[i],
          'prev-word-is-one-char': len(tokens[i-1]) == 1}

featuresets = [(punct_features(tokens, i), (i in boundaries))
                for i in range(1, len(tokens)-1)
                if tokens[i] in '.?!']

size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)

def ie_preprocess(document):
  sentence = ie_preprocess_sent(document)
  #return sentence

  #grammar = "NP: {<DT>?<JJ>*<NN>}"
  grammar = r"""
  NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and noun
      {<NNP>+}                # chunk sequences of proper nouns
"""
  cp = nltk.RegexpParser(grammar)
  chunked = []
  for line in sentence:
    #breakpoint()
    chunked.append(cp.parse(line))

  breakpoint()
  return chunked

def ie_preprocess_sent(document):
  # sentences = nltk.sent_tokenize(document)
  # sentences = [nltk.word_tokenize(sent) for sent in sentences]
  #sentences = [nltk.pos_tag(sent) for sent in sentences]

  # sentences = segment_sentences(sentences)
  # return sentences
  word_tokens = word_tokenize(document)
  #filtered_sentence = [w for w in word_tokens if not w in stop_words]

  filtered_sentence = []

  for w in word_tokens:
    if w not in stop_words:
      filtered_sentence.append(w)



  sentences =  segment_sentences(filtered_sentence)
  # sentences = [nltk.word_tokenize(sent) for sent in sentences]
  sentences = [nltk.pos_tag(sent) for sent in sentences]
  return sentences

def segment_sentences(words):
  
  start = 0
  sents = []
  for i, word in enumerate(words):
      if word in '.?!' and classifier.classify(punct_features(words, i)) == True:
          sents.append(words[start:i+1])
          start = i+1
  if start < len(words):
      sents.append(words[start:])
  #breakpoint()
  return sents
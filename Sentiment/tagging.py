import nltk
from nltk.corpus import stopwords
from nltk.tag.stanford import StanfordPOSTagger, StanfordNERTagger

class StopWords(object):
    def __init__(self):
        self.textList = []
        self.stop = stopwords.words('english')
        self.addList1 = ['again', 'between', 'above', 'below', 'over', 'under', 'further', 'all', 'any', 'both']
        self.addList2 = ['few', 'more', 'most', 'some', 'no', 'nor', 'not', 'same', 'very', 'too', 'each']
        self.stop = list(set(self.stop) - set(self.addList1))
        self.stop = list(set(self.stop) - set(self.addList2))

    def clean_sentence(self, text):
        """
        input format: 'this is a sentence. this is another one.'
        output format: cleaned sentence
            e.g.: 'this sentence. this another one.'
        """
        for word in text.split():
            if word not in self.stop:
                self.textList.append(word)
        return ' '.join(self.textList)

class Splitter(object):
    def __init__(self):
        self.nltk_splitter = nltk.data.load('tokenizers/punkt/english.pickle')
        self.nltk_tokenizer = nltk.tokenize.TreebankWordTokenizer()

    def split(self, text):
        """
        input format: a paragraph of text
        output format: a list of lists of words.
            e.g.: [['this', 'is', 'a', 'sentence'], ['this', 'is', 'another', 'one']]
        """
        sentences = self.nltk_splitter.tokenize(text)
        tokenized_sentences = [self.nltk_tokenizer.tokenize(sent) for sent in sentences]
        return tokenized_sentences


class POSTagger(object):
    def __init__(self):
        self.postagger = StanfordPOSTagger('./postagger/models/english-bidirectional-distsim.tagger', './postagger/stanford-postagger.jar')

    def pos_tag(self, sentences):
        """
        input format: list of lists of words
            e.g.: [['this', 'sentence'], ['this', another', 'one']]
        output format: list of lists of tagged tokens. Each tagged tokens has a
        form, and a list of tags
            e.g: [[(u'This', u'DT'), (u'sentence', u'NN'), (u'.', u'.')],
                    [(u'This', u'DT'), (u'another', u'DT'), (u'one', u'CD'), (u'.', u'.')]]
        """

        pos = [self.postagger.tag(sentence) for sentence in sentences]
        return pos

class NERTagger(object):
    def __init__(self):
        self.nertagger = StanfordNERTagger('./nertagger/classifiers/english.muc.7class.distsim.crf.ser.gz', './nertagger/stanford-ner.jar')

    def ner_tag(self, sentences):
        """
        input format: list of lists of words
            e.g.: [['this', 'sentence'], ['this', 'another', 'one']]
        output format: list of lists of tagged tokens. Each tagged tokens has a
        form, a lemma, and a list of tags
            e.g: [[(u'This', u'O'), (u'sentence', u'O'), (u'.', u'O')],
                    [(u'This', u'O'), (u'another', u'O'), (u'one', u'O'), (u'.', u'O')]]
        """

        ner = [self.nertagger.tag(sentence) for sentence in sentences]
        return ner

def main():
    text = "This is a sentence. This is another one."
    # remove stop words
    stopWordsObj = StopWords()
    stopRemoved = stopWordsObj.clean_sentence(text)
    # get tokenized setence
    splitterObj = Splitter()
    tokenized_sentences = splitterObj.split(stopRemoved)
    # get the Part of Speech Tag
    posTaggerObj = POSTagger()
    pos = posTaggerObj.pos_tag(tokenized_sentences)
    print pos
    # get the Named Entity
    nerTaggerObj = NERTagger()
    ner = nerTaggerObj.ner_tag(tokenized_sentences)
    print ner

if __name__ == "__main__":
    main()

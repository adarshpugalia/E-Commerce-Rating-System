import tagging as tag

class BagOfWords(object):
    def __init__(self):
        self.posTagDict = {"ADJECTIVE":["JJ", "JJR", "JJS"], "NOUN":["NN", "NNS", "NPS", "NP"], "ADVERB":["RB", "RBR", "RBS"], "VERB":["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]}
        self.nouns = set([])
        self.adjectives = set([])
        self.adverbs = set([])
        self.verbs = set([])

    def updateBagOfWords(self, text):
        stopWordsObj = tag.StopWords()
        stopRemoved = stopWordsObj.clean_sentence(text)

        splitterObj = tag.Splitter()
        tokenized_sentences = splitterObj.split(stopRemoved)

        posTaggerObj = tag.POSTagger()
        posTaggedSentences = posTaggerObj.pos_tag(tokenized_sentences)

        for sentence in posTaggedSentences:
            for word in sentence:
                lowerWord = word[0].lower()

                if(word[1] in self.posTagDict["NOUN"]):
                    self.nouns.add(lowerWord)
                elif word[1] in self.posTagDict["ADJECTIVE"]:
                    self.adjectives.add(lowerWord)
                elif word[1] in self.posTagDict["ADVERB"]:
                    self.adverbs.add(lowerWord)
                elif word[1] in self.posTagDict["VERB"]:
                    self.verbs.add(lowerWord)


    def getBagOfWords(self):
        return (self.nouns, self.adjectives, self.verbs, self.adverbs)
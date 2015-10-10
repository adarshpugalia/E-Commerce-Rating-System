import nltk
from tagging import *
from dictionaryTagger import *

class SentimentScore(object):
    def __init__(self):
        pass

    def value_of(self, sentiment):
        if sentiment == 'positive':
            return 1
        if sentiment == 'negative':
            return -1
        else:
            return 0

    def sentence_score(self, sentence_tokens, previous_token, acum_score):
        if not sentence_tokens:
            return acum_score
        else:
            current_token = sentence_tokens[0]
            tags = current_token[2]
            token_score = sum([self.value_of(tag) for tag in tags])
            if previous_token is not None:
                previous_tags = previous_token[2]
                if 'inc' in previous_tags:
                    token_score *= 2.0
                elif 'dec' in previous_tags:
                    token_score /= 2.0
                elif 'inv' in previous_tags:
                    token_score *= -1.0
            return self.sentence_score(sentence_tokens[1:], current_token, acum_score + token_score)

    def sentiment_score(self, review):
        return sum([self.sentence_score(sentence, None, 0.0) for sentence in review])


def main():
    text = "What can I say about this place. The staff of the restaurant is nice and the eggplant is not bad. Apart from that, very uninspired food, lack of atmosphere and too expensive. I am a staunch vegetarian and was sorely dissapointed with the veggie options on the menu. Will be the last time I visit, I recommend others to avoid."
    # remove stop words
    stopWordsObj = StopWords()
    stopRemoved = stopWordsObj.clean_sentence(text)
    # get tokenized setence
    splitterObj = Splitter()
    tokenized_sentences = splitterObj.split(stopRemoved)
    # # get the Part of Speech Tag
    posTaggerObj = POSTagger()
    pos = posTaggerObj.pos_tag(tokenized_sentences)
    # tag with review dictionary
    paths = ['dicts/positive.yml', 'dicts/negative.yml', 'dicts/inc.yml', 'dicts/dec.yml', 'dicts/inv.yml']
    dictTag = DictionaryTagger(paths)
    dict_tagged_sentences = dictTag.tag(pos)
    # get score by value
    sentimerntScore = SentimentScore()
    print sentimerntScore.sentiment_score(dict_tagged_sentences)


if __name__ == "__main__":
    main()

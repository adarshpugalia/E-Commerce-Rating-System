import bag_of_words as BOW

def main():
    bagOfWords = BOW.BagOfWords()

    with open("./reviews_Cell_Phones_and_Accessories.json") as f:
        for line in f:
        	x = eval(line)
        	if 'reviewText' in x.keys():
                	review = x["reviewText"]
                    bagOfWords.update_bag_of_words(review)

    words = bagOfWords.getBagOfWords()

    f = open('nouns.txt', 'w')
    for noun in words[0]:
        f.write(str(noun)+"\n")
    f.close()

    f = open('adjectives.txt', 'w')
    for adjective in words[1]:
        f.write(str(adjective)+"\n")
    f.close()

    f = open('verbs.txt', 'w')
    for verb in words[2]:
        f.write(str(verb)+"\n")
    f.close()

    f = open('adverbs.txt', 'w')
    for adverb in words[3]:
        f.write(str(adverb)+"\n")
    f.close()


if __name__ == "__main__":
    main()

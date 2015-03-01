#! /usr/bin/env python

from emojiDict import emojiLookup
import cPickle as pickle
from collections import OrderedDict
import string

class Pyemoji(object):

    def __init__(self):
        self.origEmojiDict = emojiLookup()
        # Need to make this path generic
        self.word2emoji = pickle.load(open('word2emoji.p', 'rb'))

    def printAll(self):
        """Print out the keys and symbols """
        for key in self.origEmojiDict.keys():
            print key, self.origEmojiDict[key]

    def run(self, inString):
        """Take a string, and try out replacements """

        words = inString.split(' ')
        wordsAndPhrases = []
        for i,word in enumerate(words[:-3]):
            wordsAndPhrases.append(word)
            wordsAndPhrases.append(words[i]+' '+words[i+1])
            wordsAndPhrases.append(words[i]+' '+words[i+1]+' '+words[i+2])

        wordsAndPhrases.append(words[-2]+' '+words[-1])
        wordsAndPhrases.append(words[-3])
        wordsAndPhrases.append(words[-2])
        wordsAndPhrases.append(words[-1])

        results = OrderedDict()

        # Need to strip out punctuation (. , " !, etc)
        # Need to check for plurals.
        counter = 0
        for phrase in wordsAndPhrases:
            ph = phrase.translate(string.maketrans("",""), string.punctuation).lower()
            # Check if it ends in 's' and look for singular version
            if ph in self.word2emoji.keys():
                results[phrase+' '+str(counter)] = self.word2emoji[ph]
            elif ph[:-1] in self.word2emoji.keys():
                results[phrase+' '+str(counter)] = self.word2emoji[ph[:-1]]
            else:
                if ' ' not in phrase:
                    results[phrase+' '+str(counter)] = phrase
            counter += 1

        self.results = results

    def printResults(self):
        """
        Print the results out in a pretty way
        """

        # Print the key value pairs
        for key in self.results.keys():
            ack = key.split(' ')
            ack = ack[:-1]
            ack = ''.join(ack)
            print ack, ' '.join(self.results[key])


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Tool to help convert a string into emoji symbols.")
    parser.add_argument("inString", type=str, help="String to convert into emoji symbols.")
    args = parser.parse_args()

    myemoji = Pyemoji()
    myemoji.run(args.inString)
    myemoji.printResults()

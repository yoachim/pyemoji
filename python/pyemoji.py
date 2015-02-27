#! /usr/bin/env python

from emojiDict import emojiLookup
import cPickle as pickle
from collections import OrderedDict

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
        wordsAndPhrases.append(words[-1])

        results = OrderedDict()

        # Need to strip out punctuation (. , " !, etc)
        # Need to check for plurals.
        counter = 0
        for phrase in wordsAndPhrases:
            if phrase in self.word2emoji.keys():
                results[phrase+' '+str(counter)] = self.word2emoji[phrase]
            else:
                if ' ' not in phrase:
                    results[phrase+' '+str(counter)] = phrase
            counter += 1

        return results


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Tool to help convert a string into emoji symbols.")
    parser.add_argument("inString", type=str, help="String to convert into emoji symbols.")
    args = parser.parse_args()

    myemoji = Pyemoji()
    result = myemoji.run(args.inString)

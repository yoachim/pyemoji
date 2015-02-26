from emojiDict import emojiLookup
import cPickle as pickle

class pyemoji(object):

    def __init__(self):
        self.origEmojiDict = emojiLookup()
        # Need to make this path generic
        word2emoji = pickle.load(open('word2emoji.p', 'rb'))

    def printAll(self):
        """Print out the keys and symbols """
        for key in self.origEmojiDict.keys():
            print key, self.origEmojiDict[key]

    def run(self, inString):
        """Take a string, and try out replacements """

        words = inString.split(' ')
        wordsAndPhrases = []
        for i,word in enumerate(words[:-3]):
            wordsAndPhases.append(word)
            wordsAndPhases.append(words[i]+' '+words[i+1])
            wordsAndPhases.append(words[i]+' '+words[i+1]+' '+words[i+2])
        wordsAndPhases.append(words[-2]+' '+words[-1])
        wordsAndPhases.append(words[-1])

        results = [ ]

        for phrase in wordsAndPhases:
            results.append((word) )


if __name__="__main__":

    # arg parse the strings and run it.

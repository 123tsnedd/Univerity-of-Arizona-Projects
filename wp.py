from words import Words
class WordProcessor:

    def __init__(self, filename):
        self.filename = filename
        self.vocabulary = []
        self.wordcount = -1
    
    def load_string_from_file(self):
        """ Read words from filename, return a string
            composed of the file content.
        """
        f = open(self.filename, "r")
        file_content = f.read()
        f.close()
        return file_content 
    
    def processText(self, text):
        words = Words(text)
        wds = words.getWords()
        self.wordcount = len(wds)
        deduplicated_words = words.remove_dups()
        deduplicated_words.sort()
        self.vocabulary = deduplicated_words

    def getWordcount(self):
        """ Return the number of words extracted from the file. 
            Note that the duplicate words are also counted
        """
        return self.wordcount

    def getVocabulary(self):
        """ Return the vocabulary extracted from the file. 
            Note that there is no duplicate word contained in the vocabulary  
        """
        return self.vocabulary
    

    
wp = WordProcessor("brooks.txt")
filecontent = wp.load_string_from_file()

wp.processText(filecontent)
print(wp.getWordcount())
print(wp.getVocabulary())

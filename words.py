class Words:
    
    def __init__(self, the_text=""):
        self.the_text = the_text
        if (the_text !=""):
            self.words = self.text_to_words()
        else:
            self.words = []
            
    def setText(self, the_text):
        self.the_text = the_text
        
    def getWords(self):
        return self.words
    
    def text_to_words(self):
        """ return a list of words with all punctuation and numbers removed,
            and all in lowercase based on the given text string.
        """
        my_substitutions = str.maketrans(
          # If you find any of these
          "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
          # Replace them by these
          "abcdefghijklmnopqrstuvwxyz                                          ")

        # Translate the text now.
        cleaned_text = self.the_text.translate(my_substitutions)
        wds = cleaned_text.split()
        return wds

    def remove_dups(self):
        """ Return a new list in which all duplicates 
            from the words, have been removed.
        """
        word_list = self.words
        new_list = [] 
        for elem in word_list:
            if elem not in new_list:
                new_list.append(elem)
        return new_list




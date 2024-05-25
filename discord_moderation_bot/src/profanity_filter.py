# profanity_filter.py

import profanity_filter

class ProfanityFilter:
    
    def __init__(self):
        self.filter = profanity_filter.ProfanityFilter()

    def censor_message(self, message):
        return self.filter.censor(message)

    def check_profanity(self, message):
        return self.filter.has_profanity(message)

    def add_profanity(self, word):
        self.filter.add_word(word)

    def remove_profanity(self, word):
        self.filter.remove_word(word)
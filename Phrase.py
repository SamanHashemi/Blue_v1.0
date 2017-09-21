class Phrase:

    def __init__(self, trigger_words, priority, function):
        self.trigger_words = trigger_words
        self.priority = priority
        self.function = function

    def get_trigger_words(self):
        return self.trigger_words

    def get_priority(self):
        return self.priority

    def get_function(self):
        return self.function

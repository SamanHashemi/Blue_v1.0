import random
class Hello:
    trigger_words = ["hello", "hi", "hey"]
    # Put an input list with rankings for specfic features (slang, aggresvie, shy, etc)
    def __init__(self):
        self.trigger_words = ["hello", "hi", "hey"]
        self.priority = 0

    def hello(self):
        # pass
        responses = ['hi', 'hello', 'hello there', 'hey', 'hey! how can I help']
        #TODO: Build tagging system for the words and then put in the most appropriate word via tag
        return responses[random.randint(0, len(responses)-1)]
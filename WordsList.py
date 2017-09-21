from Phrase import Phrase as phrase
import os
import imp

class WordsList:
    def __init__(self):
        self.phrase_list = []

    def create_list(self):
        directory = os.path.dirname("/Users/Saman-Mac/Desktop/Projects/SpeechRecognition/src/Actions/")

        skipper = 0
        for filename in os.listdir(directory):
            if skipper == 0:
                skipper += 1
                pass
            else:
                module_name = imp.load_source(filename, os.path.join(directory, filename))  # Module name
                class_name = str(filename)[:-3]  # Class name of each module
                class_ref = getattr(module_name, class_name)()  # Reference to module's class
                function_name = str(filename)[:-3].lower()  # Name of the module's function
                function_ref = getattr(class_ref, function_name)  # Reference to that function
                # self.word_func_dict[class_ref.trigger_words] = function_ref
                self.phrase_list.append(phrase(class_ref.trigger_words, class_ref.priority, function_ref))

    def search_list(self, spoken_phrase):
        cur_matched_words = 0
        max_matched_words = 0
        current_priority = 0
        matched_phrase = None
        for cur_phrase in self.phrase_list:  # For the list of tuple words in the word_func_dict
            for word in cur_phrase.get_trigger_words():  # For each word in the tuple of the of word_func_dict
                if word in spoken_phrase.split():  # If the word is in the phrase spoken
                    cur_matched_words += 1
                if cur_matched_words > max_matched_words:  # If the current # of matched words is > than the max_matched
                    max_matched_words = cur_matched_words
                    matched_phrase = cur_phrase
                elif cur_matched_words == max_matched_words:  # If cur_matched == the max matched
                    if cur_phrase.get_priority() > current_priority:  # Check each priority level
                        current_priority = cur_phrase.get_priority()  # Change the priority level of the current word
                        max_matched_words = cur_matched_words  # Change the value of the max_matched to the new max
                        matched_phrase = cur_phrase  # The current word is the phrase
            cur_matched_words = 0
        return matched_phrase

from STT import STT
from WordsList import WordsList
from TTS import TTS



class Brain:

    def __init__(self):
        pass

    def run(self):
        wordList = WordsList()
        wordList.create_list()
        stt = STT()
        tts = TTS()

        print("Say something")
        phrase_said = ""
        function_called = True

        while phrase_said.lower() != "Exit".lower():
            phrase_said = stt.phrase_spoken()
            try:
                print("You said: " + phrase_said)
            except TypeError:
                phrase_said = ""
                print(".")
            if 'Blue'.lower() in phrase_said.lower():
                # Make chime
                tts.speak("Yes?")
                print("Blue: Yes?")
                # Pause Here (...but how???) Use a continue function like the one on the raspberry pi
                phrase_said = stt.phrase_spoken()  # Save the text of the user's audio
                try:  # try to get a response if one exists
                    print("You: " + phrase_said)  # Tell user what they said
                    corresponding_phrase = wordList.search_list(phrase_said)  # Get the corresponding phrase object
                    response = (corresponding_phrase.get_function())()  # Get the phrase
                except TypeError:  # If no audio was detected
                    response = "Sorry Lucy didn't quite catch that"
                    phrase_said = ""
                except AttributeError:  # If the word does not exist in the word list
                    response = "Sorry I am not advanced enough to answer that"
                    phrase_said = ""

                print("Blue: " + str(response))
                tts.speak(response)
        # elif "Lucy".lower() in phrase_said.lower():
            # Go through list and find appropriate function


brain = Brain()
brain.run()

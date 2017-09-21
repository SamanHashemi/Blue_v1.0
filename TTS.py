from gtts import gTTS
import pyglet


"""TODO: Set up offline speech recogniton
thorugh pocketsphynx"""
class TTS:
    def __init__(self):
        pass

    def speak(self, text_to_speak):  # Speak the text passed
        tts = gTTS(text=text_to_speak, lang='en')
        tts.save("response.mp3")
        try:
            response = pyglet.media.load("response.mp3")
            response.play()
        except:
            print("response could not load")

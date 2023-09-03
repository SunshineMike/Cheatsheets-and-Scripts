import pyttsx3


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.set_rate(-50)
        self.set_volume(0.7)

    def set_rate(self, change):
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate + change)

    def set_volume(self, volume):
        self.engine.setProperty('volume', volume)

    def set_voice(self, voice_id):
        self.engine.setProperty('voice', voice_id)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def test_voices(self):
        voices = self.engine.getProperty('voices')
        for voice in voices:
            print(voice)
            self.set_voice(voice.id)
            self.engine.say('The quick brown fox jumped over the lazy dog.')
        self.engine.runAndWait()


'''
tts = TextToSpeech()
tts.test_voices()
tts.speak("Hello, world!")
'''
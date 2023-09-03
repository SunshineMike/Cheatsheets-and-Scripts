import speech_recognition as sr


class SpeechRecognizer:
    def __init__(self, debug=False):
        self.recognizer = sr.Recognizer()
        self.debug = debug


def listen(self):
    while True:
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
                print("Listening...")
                audio = self.recognizer.listen(source)

                text = self.recognizer.recognize_google(audio)
                text = text.lower()

                if debug:
                    print(" -- Rec: ", text)

                return text

            except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

            except sr.UnknownValueError:
            print("Unknown error occurred")

'''
speech = SpeechRecognizer(debug=True)
text = speech.listen()
'''
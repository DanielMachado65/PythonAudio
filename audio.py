#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import speech_recognition as sr


class Method(object):
    """
    Classe que serve como parâmetro para criação de leitor de voz de python.
        + Use API of the google api
            - SpeechRecognition
    """

    __author__ = "Daniel Machado"
    r = sr.Recognizer()

    def audioretprontile(self, name):
        # Get audio
        harvard = sr.AudioFile(name)
        with harvard as source:
            audio = self.r.record(source)
            type(audio)
            self.r.recognize_google(audio)

    def audiorecord(self):
        # Record Audio
        with sr.Microphone() as source:
            print("Say something!")
        self.r.adjust_for_ambient_noise(source)
        while True:
            audio = self.r.listen(source)
            try:
                print("You said: " + self.r.recognize_google(audio))
            except sr.UnknownValueError and sr.RequestError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))


if __name__ == '__main__':
    a = Method()
    a.audioretprontile('english.wav')

    r = sr.Recognizer()
    harvard = sr.AudioFile('english.wav')
    with harvard as source:
        audio = r.record(source)
        type(audio)
        print(r.recognize_google(audio))

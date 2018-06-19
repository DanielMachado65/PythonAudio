import speech_recognition as sr


class Audio(object):
    """
    Class which propuse is reader of file voice on Python
        + Use API of the google api
            - SpeechRecognition

    PT-BR:
        Classe que serve como parâmetro para criação de leitor de voz de python.
            + Use API of the google api
                - SpeechRecognition - reconhecimento da classe
    """
    __author__ = "Daniel Machado"
    r = sr.Recognizer()

    def audiomanipulation(self, path):
        """
        Fuction return the string of filePath
        :param path:
        :return:
        """
        file = sr.AudioFile(path)
        with file as source:
            audio = self.r.record(file)
            return self.r.recognize_google(audio, language='pt')

    def audiorecord(self):
        """
        Function record the voice
        :return: none
        """
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            print("Diga alguma coisa...")
            audio = self.r.listen(source)
            fala = self.r.recognize_google(audio, language="pt")
            while fala != 'sair':
                if audio is not None:
                    try:
                        print(self.r.recognize_google(audio, language="pt"))
                    except sr.UnknownValueError as error:
                        print("O google não conseguiu entender o que foi falado" + error)
                    except sr.RequestError as e:
                        print("Não foi possivel ter resultados do Google Speech Recogntition; {0}".format(e))
                audio = self.r.listen(source)
                fala = self.r.recognize_google(audio, language="pt")


if __name__ == '__main__':
    Exe = Audio()
    print("començando a execução")
    Exe.audiorecord()

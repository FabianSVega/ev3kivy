from asyncio import threads
import kivy
from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
import webbrowser as wb
import speech_recognition as sr
import socket
import time
import threading

micro = sr.Microphone()   
r = sr.Recognizer()

Window.size = (385, 520)

Builder.load_file('./details.kv')    

class work(Widget, threading.Thread):
    
    def __init__(self, **kwargs):
        super(work, self).__init__(**kwargs)
        
    def thr(self):
        t=threading.Thread(target=self.try_one)
        t.start()
    def word(self):
        w=threading.Thread(target=self.palabra)
        w.start()

    def palabra(self):
        with micro as source:
            print("Porfavor hable fuerte y claro")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            fraseDicha = r.recognize_google(audio,language='es-CO')
            self.ids.input_n.text = "Usted ha dicho "+fraseDicha
    
    def cerrar(self):
        work().stop()
        
    def server(self):
        HostName = socket.gethostname()
        direccionIp = socket.gethostbyname(socket.gethostname())
        self.ids.input_n.text ="HostName: "+ HostName + " con numero IP :"+direccionIp

    
    def try_one(self):
        micro = sr.Microphone()   
        r = sr.Recognizer()
        with micro as source:
            print("Porfavor hable fuerte y claro")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            fraseDicha = r.recognize_google(audio,language='es-CO')  
            if fraseDicha == "Ayuda":
              self.ids.input_n.text = "la palabra dicha fue ayuda"
            elif fraseDicha == "ayuda":
             self.ids.input_n.text = "la palabra dicha fue ayuda"
            elif fraseDicha == "Auxilio":
             self.ids.input_n.text = "la palabra dicha fue auxilio"
            elif fraseDicha  == "auxilio":
             self.ids.input_n.text = "la palabra dicha fue auxilio"
            elif fraseDicha == "Socorro":
              self.ids.input_n.text = "la palabra dicha fue socorro"
            elif fraseDicha == "socorro":
              self.ids.input_n.text = "la palabra dicha fue socorro"
            else:
             self.ids.input_n.text = "Se ha dicho una palabra distinta a las especificas"
            return fraseDicha           
                  

      
class workapp(App):
    def build(self):
        return work()


if __name__ == '__main__':
    workapp().run()
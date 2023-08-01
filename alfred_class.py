import os   #system lib
import speech_recognition as sr   #converts speech to text
from playsound import playsound    #plays .mp3 files
import time
from gtts_sounds import play_audio

class Alfred:
    
    def activate_mic(self):
        #opening the standard pc mic
        mic = sr.Recognizer()
        with sr.Microphone() as source:
            mic.adjust_for_ambient_noise(source)
            
            audio_input = mic.listen(source)
            
            #verifying if the text is recognizable
            try: to_text_input = mic.recognize_google(audio_input, language = 'pt-BR')
            
            except sr.UnknownValueError:
                path = os.path.join('alfreds_sounds', 'error.mp3')
                path = os.path.normpath(os.path.join(os.getcwd(), path))
                playsound(path)
                
                #delaying the execution of the code
                time.sleep(3)
                
                return self.activate_mic()
            
            #verifying the output
            print(to_text_input)
            
            return to_text_input
    
    def main_alfred(self, second_part=False):
            
        if second_part == False:    
            path = os.path.abspath(os.path.join('alfreds_sounds', 'talk.mp3'))
            playsound(path)
        else:
            play_audio('O que vai querer?', 'secpart.mp3')
        
        text = self.activate_mic()
        
        for word in text.split(' '):
            #if there is a quit word in text
            if word in self.quit_words:
                self.quit = True
                return
            
            #if there is an init_word in text in the first run
            if word in self.init_words and second_part==False:
                return self.main_alfred(second_part=True)
                
            if second_part and word in self.order_words:
                play_audio('Qual vai ser o pedido?', 'whatstheorder.mp3')
                
                text = self.activate_mic()
                
                #ordering
                if 'último' in text:
                    print('ultimo')
                    return
                if 'rápido' in text:
                    print('rapido')
                    return
                if 'padrão' in text:
                    print('padrão')
                    return
                
                play_audio('não entendi')
                
                return self.main_alfred(second_part=False)
        
    #constructor
    def __init__(self):
        self.init_words = ['pedido', 'comida', 'fome']      #list of 'positive for search' words
        self.order_words = ['normal', 'sempre', 'mesmo']
        self.quit_words = ['Cancelar', 'Parar', 'Cancela', 'Esquece']                         #list of 'negative for search' words => quit()
        self.search = []    #array with searching parameters
        self.quit = False                                                                             #quit confirmation set to False
          
        self.main_alfred()      #calls for the main function in self
        
alfie = Alfred()
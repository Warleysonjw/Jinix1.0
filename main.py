# Our main file.

import speech_recognition as sr

# Criar um reconhecedor
r = sr.Recognizer()

#Abrir um microfone
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    while True:
       audio = r.listen(source) # Definemicrofone como fonte de áudio
    
       print(r.recognize_google(audio,language='pt'))

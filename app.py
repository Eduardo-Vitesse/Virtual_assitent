from pynput.keyboard import Key, Controller
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import time

record = sr.Recognizer()
keyboard = Controller()

voice_start = gTTS('Qual programa deseja abrir?',lang='pt')
voice_start.save('audios/hello.mp3')
playsound('audios/hello.mp3')

with sr.Microphone() as fonte:
    print('Running...')
    audio = record.listen(fonte)
    text = record.recognize_google(audio, language='pt-BR')

voice_midle = gTTS(f"Abrindo {text.capitalize()}",lang='pt')
voice_midle.save('audios/midle.mp3')
playsound('audios/midle.mp3')

keyboard.press(Key.cmd)
keyboard.release(Key.cmd)
time.sleep(3)
keyboard.type(f'{text.capitalize()}')
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

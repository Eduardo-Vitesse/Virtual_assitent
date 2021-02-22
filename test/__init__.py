import speech_recognition as sr
from pynput.keyboard import Key, Controller
import time
from gtts import gTTS
from playsound import playsound

record = sr.Recognizer()
keyboard = Controller()

while True:
    with sr.Microphone() as voice_start:
        print('Estou ouvindo 01...')
        audio_start = record.listen(voice_start)
        text_resp = record.recognize_google(audio_start, language='pt-BR')

    if 'assistente' or 'Assistente' in text_resp.capitalize():
        voice_start = gTTS("Estou ouvindo, qual programa deseja abrir?",lang='pt-br')
        voice_start.save('hello.mp3')
        playsound('hello.mp3')

        with sr.Microphone() as fonte:
            print('Estou ouvindo 02...')
            audio = record.listen(fonte)
            text = record.recognize_google(audio, language='pt-BR')

            voice_midle = gTTS(f"Abrindo {text.capitalize()}",lang='pt-br')
            voice_midle.save('midle.mp3')
            playsound('midle.mp3')

        keyboard.press(Key.cmd)
        keyboard.release(Key.cmd)
        time.sleep(3)
        keyboard.type(f'{text.capitalize()}')
        time.sleep(3)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(3)
        voice_end = gTTS(f"Prontinho, qualquer coisa é só chamar",lang='pt-br')
        voice_end.save('soundEnd.mp3')
        playsound('soundEnd.mp3')
        time.sleep(5)

    elif 'encerrar' or 'Encerrar' in text_resp.capitalize():
        break
    else:
        pass

#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import speech_recognition as sr
#import keyboard
# import the core lib
from core import SystemInfo
from core.system import Runner
# import classifier
from NLU.classifier import classify

# Speech Synthesis
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# changing index, changes voices. 1 for female and 0 for male
engine.setProperty('voice', voices[1].id)


def evaluate(text):
    entity = classify(text)
    if entity == 'time\getTime':
        speak(SystemInfo.get_time())
    elif entity == 'time\getDate':
        speak(SystemInfo.get_date())
    elif entity == 'music\playPause':
        SystemInfo.play_pause()
    elif entity == 'open\notepad':
        speak('ok, opening notepad')
        os.system('notepad.exe')
    elif entity == 'open\chrome':
        speak('ok, opening google chrome')
        SystemInfo.open_chrome()

    else:
        exit()


def speak(text):
    engine.say(text)
    engine.runAndWait()


'''
model = Model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1,
                rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()


while True:
    data = stream.read(8192)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        # convert result from string to dict
        result = json.loads(rec.Result())
        text = result['text']
        print(text)
        evaluate(text)
'''

# google recognizer


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        print("Say that again please...")
        return "None"  # None string will be returned
    return query.lower()


if __name__ == "__main__":
    while(True):
        evaluate(takeCommand())

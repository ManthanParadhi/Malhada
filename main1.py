#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
# import the core lib
from core import SystemInfo

# Speech Synthesis
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# changing index, changes voices. 1 for female and 0 for male
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


model = Model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1,
                rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(8000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        # convert result from string to dict
        result = json.loads(rec.Result())
        text = result['text']
        if "time" in text:
            speak(SystemInfo.get_time())

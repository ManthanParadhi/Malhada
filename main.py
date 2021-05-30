#import libraries
import speech_recognition as sr
r = sr.Recognizer()
# Get the default microphone
with sr.Microphone() as source:
    # Listen to command, using

    while True:
        audio = r.listen(source)
        # Recognizes speech using Google as a Service: Online
        text = r.recognize_google(audio)
        print(text)

#import libraries
import speech_recognition as sr
r = sr.Recognizer()
# Get the default microphone
with sr.Microphone() as source:
    # Listen to command, using

    while True:
        audio = r.listen(source)
        # Recognizes speech using Google as a Service: Online
        try:
            google = r.recognize_google(audio)
            sphinx = r.recognize_sphinx(audio)
            print("Google:{}\nSphinx:{}\n\n".format(google, sphinx))
        except:
            print("Cannot Recognize your language")
        break

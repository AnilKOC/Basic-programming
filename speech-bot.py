import speech_recognition as sr
import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")
r = sr.Recognizer()

def listener():
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except:
            speak.Speak("I did not understand, could you repeat it?")
            listener()
        return text
            
speak.Speak("What's your name?")
name=listener()
text=("Hello ",name," how are you?")
speak.Speak(text)
speak.Speak("Do you have a question?")
question=listener()
if question == "who is your god": speak.Speak("My god is Anıl")
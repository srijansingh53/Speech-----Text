import speech_recognition as sr
r=sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something");
    audio=r.listen(source)
    print("Time Over, Thanks")

try:
    print ("TEXT: " +r.recognize_google(audio, language='hi-IN'))
except:
    pass

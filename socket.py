import speech_recognition as sr
import socket
import pyttsx3
engine=pyttsx3.init()
mic=sr.Microphone()
rec=sr.Recognizer()
s=socket.socket()
s.connect(("192.168.43.71",8882))
engine.say("client are succesfully connected to the server")
engine.runAndWait()




with mic as source:
    print("say")
    audio=rec.listen(source)
    text=rec.recognize_google(audio)
    print(text)
    if("date" in text and "run" in text) or("date" in text and "execute" in text):
                                            ch="1"
                                            print("date")
    elif("calendar" in text and "run" in text) or("calendar" in text and "execute" in text):
                                            ch="2"
                                            print("cal")
                                              
                                            


ch=ch.encode()
s.send(ch)
finaloutput=s.recv(200)
finaloutput=finaloutput.decode()
print(finaloutput)
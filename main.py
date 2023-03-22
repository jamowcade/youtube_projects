import pyttsx3

engine =  pyttsx3.init()



engine.say("say something please!")

while True:
    answer = input("Enter your text: ")
    engine.setProperty("rate", 150)
    engine.say(answer)
    engine.runAndWait()
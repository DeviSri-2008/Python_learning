from gtts import gTTS
import os
def program1():
    t = "Hello All,How are you all."
    tts = gTTS(text = t)
    tts.save("p1_hello.mp3")
    print("Program 1: Saved p1_hello.mp3")
program1()
 

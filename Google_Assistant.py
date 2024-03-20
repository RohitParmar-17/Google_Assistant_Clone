import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import speech_recognition as sr
import pyttsx3

genai.configure(api_key="AIzaSyBLP5015glVl5FCFtJYGoAKYCs3_KmgsbU")
model = genai.GenerativeModel('gemini-pro')

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def intro(name):
  print(f"Hey {name}!, How Can I Help You?")

def def_ques(ques):
    device_list = ['alarm', 'timer', 'message', 'call']

    flag = False
    flag1 = False
    flag2 = False
    for i in device_list:
        if i in ques.lower():
            flag = True

    if flag:
        return "Not Supported Yet.\nWe Will Be Updating This Assistant Soon!!\nSTAY TUNED :)"

    else:
        if "who created you" in ques.lower() and not flag1:
            flag1 = True
            return "Nilay Koul Created Me"

        elif "what is your name" in ques.lower() or "who are you" in ques.lower() or "your name?" in ques.lower() and not flag2:
            flag2 = True
            return "I am a Google Assistant Clone\nYou Can Ask Me Any Question!"

        else:
            response = model.generate_content(ques)
            return to_markdown(response.text)

def listen_and_respond():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        question = recognizer.recognize_google(audio)
        print("You said:", question)
        
        return question
        # Process the question
        # response = def_ques(question)
        # return response
        # Speak the response
        # synthesizer.say(response)
        # synthesizer.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        print("Failed to request results. Check your internet connection.")

def Assistant():
  name = input("Hey!, What Is Your Name?\n")
  intro(name)
  STOP = True
  while STOP:
    ques=listen_and_respond()
    if "stop" in ques:
      STOP = False
      break
    response = def_ques(ques)
    print(response.data)

Assistant()
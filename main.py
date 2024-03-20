import pathlib
import textwrap
from gtts import gTTS
import google.generativeai as genai
from IPython.display import display, Audio
from IPython.display import Markdown

genai.configure(api_key="YOUR_GENERATED_KEY")
model = genai.GenerativeModel('gemini-pro')

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def intro(name):
  print(f"Hey {name}!, How Can I Help You?")

def def_ques(ques):
  device_list = ['alarm', 'timer', 'message', 'call']

  flag = False

  for i in device_list:
    if i in ques.lower():
      flag = True

  if flag == True:
    return("Not Supported Yet.\nWe Will Be Updating This Assistant Soon!!\nSTAY TUNED :)")
    flag = False

  if flag == False:
    if "who created you" in ques.lower():
      return("Rohit Parmar Created Me")
    elif "what is your name" in ques.lower() or "who are you" in ques.lower() or "your name?" in ques.lower():
      return("I am a Google Assistant Clone\nYou Can Ask Me Any Questions!")
    else:
      prompt = ques + " in 40 words"
      response = model.generate_content(prompt)
      text1 = to_markdown(response.text)
      print(display(text1))
      return text1.data
    
def text_to_audio(text, filename="output.mp3"):
    tts = gTTS(text, lang="en")
    tts.save(filename)
    print(f"Audio file '{filename}' created successfully!")
    display(Audio("output.mp3", autoplay=True))

def Assistant():
  name = input("Hey!, What Is Your Name?\n")
  intro(name)
  STOP = True
  while STOP:
    ques=(input())
    if "stop" in ques:
      STOP = False
      break
    response = def_ques(ques)
    print("Response:", response)
    if response is not None and response.strip():
        text_to_audio(str(response))
    else:
        print("Empty or None response. Skipping audio generation.")

Assistant()

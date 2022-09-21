import pyttsx3
import os
import wikipedia
import datetime
import webbrowser
import pywhatkit
import speech_recognition as sr
import pyautogui as pt
from time import sleep
import pyperclip as pp
from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options
from googletrans import Translator
query_hin=""
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
rate=engine.getProperty('rate')
engine.setProperty('rate',150)

print(voices)
engine.setProperty('voice', voices[2].id)
def speak(audio):
 engine.say(audio)
 engine.runAndWait()
def wishme():
 t=datetime.datetime.now().hour
 if t>=4 and t<12:
  speak("गुड मॉर्निंग पांडे जी")
 elif t>=12 and t<17:
  speak("गुड आफ्टरनून पांडे जी")
 else:
  speak("गुड इवनिंग पांडे जी ")
 speak("मैं देव हूँ।  मैं आपकी मदद कैसे कर सकता हूं सर")
def takecommand():
 translator= Translator()
 r=sr.Recognizer()
 while True:
     with sr.Microphone() as source:
      print("Go on i am listening...")
      r.adjust_for_ambient_noise(source, duration=1)
      r.pause_threshold=3
      audio=r.listen(source)
     try:
      global query_hin
      print("Recognizing...")
      print("Audio पहचान प्रक्रिया में है")
      query_en=r.recognize_google(audio,language='en-in')
      query_hin=r.recognize_google(audio, language='hi-in')
      return query_en
     except Exception as e:
      print(e)
      print("Please speak again")
      speak("कृपया फिर से बोलें")
      query_en=None
      pass
      
  
 
while True:
 main=str(takecommand().lower())
 if main=='activate':
  wishme()
  while True:     
        if True:
            v= str(takecommand().lower())
            q=list(v.split(" "))
            if 'youtube'in q:
             for i in q: 
              if i in ['chalao','chalaao','chalau','play']:
               speak("कृपया गाना का नाम बताएं |")
               song=takecommand().lower()
               pywhatkit.playonyt(song)
               pt.press('playpause')
              elif i in ["kholo","open"]:
                 webbrowser.open('http://www.youtube.com')
            elif "google" in q and ("kholo" in q or "open" in q):
             webbrowser.open('http://www.google.com')
            elif "kon" in q or "kya" in q or "kab" in q or "kyu" in q or "what" in q or "why" in q or "when" in q or "why" in q or "kon" in q or "who" in q :
             wikipedia.summary(v, sentences=2)
            elif "mail" in q:
             speak("किसके लिए सर ?")
             print("To whom sir?")
             to=takecommand().lower()
             speak("कृपया मुझे  message बताएं")
             message=takecommand().lower()
             server=smtplib.SMTP('smtp.gmail.com', 587)
             server.ehlo()
             server.starttls()
             server.login('sarvagyaisgood@gmail.com', 'iknowyou')
             server.sendmail
            elif "whatsapp" in q:
             speak("क्या आप किसी को मैसेज भेजना चाहते हैं सर ?")
             a=takecommand()
             a.lower()
             if ("yes" in a) or ("haa" in a) or ("haan" in a) or ("es" in a):
              speak("आप किसको मैसेज भेजना चाहेंगे सर ?")
              name= takecommand()
              speak(f"क्या आप जिसे संदेश भेजना चाहते हैं उसका नाम {name} है ? अगर हां तो  yes बोलिये और अगर नहीं तो  no बोलिये  और नाम टाइप करें")
              print(f"Is the name {name}?(yes or no)")
              a= str(takecommand().lower())
              
              if ("yes" in a) or ("haa" in a) or ("haan" in a) or ("es" in a):
               print("OK")
              else:
               name=input("नाम टाइप करें(Type the name):")
             
              name.lower()
              speak("आप क्या मैसेज भेजना चाहेंगे सर ?")
              message=takecommand()
              message.lower()
              options = webdriver.ChromeOptions()
              options.add_argument("--user-data-dir=C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\User Data\\")
              options.add_argument("profile-directory=wtsp")
              driver=webdriver.Chrome( executable_path=r'C:\Users\HP\Desktop\chromedriver.exe', options=options)
              driver.implicitly_wait(5)
              driver.get('http://web.whatsapp.com')
              driver.maximize_window()
              driver.get('http://web.whatsapp.com')
              driver.maximize_window()
              #webbrowser.open("http://web.whatsapp.com")
              sleep(10)
              while True:
               pos=pt.locateCenterOnScreen(r'C:\Users\HP\Desktop\2022-08-08.png', confidence=0.8)
               if pos==None:
                print("Loading...")
                continue
               else:
                break 
            
              pos=pt.locateCenterOnScreen(r'C:\Users\HP\Desktop\2022-08-08.png', confidence=0.8)
              pt.moveTo(pos[0:2],duration=0.3)
              pt.moveRel(-70,0)
              pt.click()
              pt.typewrite(name)
              sleep(10)
              pt.moveRel(0,200)
              pt.click()
              pos=pt.locateCenterOnScreen(r'C:\Users\HP\Desktop\2022-08-08 (2).png', confidence=0.4)
              pt.moveRel(-70,0)
              pt.click()
              pt.typewrite(message)
              sleep(10)
              pt.press('enter')
              sleep(3)
              driver.quit()
            elif 'deactivate' in q:
              break
            else:
             continue
  else:
     continue   

from webbrowser import get
import pyttsx3
import datetime, time
import speech_recognition as sr
import wikipedia
import mysql.connector
import sqlite3
from webdriver_manager.chrome import ChromeDriverManager
from googlemaps import Client as GoogleMaps
from library import wikipedia1, search1, search2, send_email, music, movie, weather, change_wallpaper, read_newspaper, tellabout
from library import youtube, song_youtube, open_webbsite, open_application, security_name, security_id, day, time_now, greeting
from library import find_location
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

path = ChromeDriverManager().install()
shield_mouse = pyttsx3.init()
voice = shield_mouse.getProperty('voices')
shield_mouse.setProperty('voice', voice[1].id)

def shield_brain(audio):
    print("S.H.I.E.L.D: " + audio)
    shield_mouse.say(audio)
    shield_mouse.runAndWait()

def shield_ear():
    shield_ear = sr.Recognizer()
    with sr.Microphone() as source:
        shield_ear.pause_threshold = 0.6
        audio = shield_ear.listen(source)
    try:
        you = shield_ear.recognize_google(audio, language="en")
        print("Boss: " + you.title())
    except sr.UnknownValueError:
        you = ""
        print("Boss: ?" + you.title())   
    return you

window = tk.Tk()
window.title("S.H.I.E.L.D")
window.geometry("800x600")
window.iconbitmap("shield.ico")

load = Image.open("background1.png")
render = ImageTk.PhotoImage(load)
img = Label(window, image= render)
img.place(x = 0, y = 0)

def db(you):
    conn = sqlite3.connect("data.sqlite")
    c = conn.cursor()   
    while True:
        if not you:
            shield_brain("SHIELD can't hear clearly.")
        else:
            you = you + "?"
            if "\'" in you:
                you = you.replace("'", "")
            c.execute(f"SELECT * FROM `table` WHERE Question = '{you}'")
            result = str(c.fetchone())
            if result != "None":
                newresult = result[1:-1]
                answer =  newresult.split(", ")[2][1:-1]
                shield_brain(answer)  
                break
            else:
                shield_brain("Sorry sir! SHIELD doesn't know how to answer you!")
                shield_brain("What is the answer to the above question?")
                newanswer = shield_ear().title()
                if "'" in newanswer:
                    newanswer = newanswer.replace("'", "")
                c.execute(f"INSERT INTO `table` (`Question`, `Answer`) VALUES ('{you}', '{newanswer.title()}.')")
                conn.commit()
                conn.close()
                shield_brain("The answer has just been added!")
                break

def main():
    # security_name()
    # security_id()
    greeting()

    while True:
        you = shield_ear().lower() 

        textBox = tk.Entry(window, width= 23, font=("ROBOT", 16), bg='#000000', fg='red', text=set(you)) 
        textBox.place(x = 87, y = 210)
        textBox.insert(0, you) 
        textBox.delete(0, END)
          
        if not you:
            shield_brain("SHIELD is listening to you! Please say!")  
        elif "shield" in you:
            you = you.replace("shield", "") 
        elif "wikipedia" in you:
            shield_brain("What do you want to find on wikipedia?")
            text = shield_ear().lower()
            wikipedia1(text)
        elif "search" in you:
            if (str(you).split("search" , 1)[1] == ""):
                search1()
            else: 
                search2(you)
        elif ("mail" in you):
            send_email()
        elif "music" in you:
            music()
        elif "movie" in you:
            movie()         
        elif "weather" in you:
            weather()
        elif "wallpaper" in you:
            change_wallpaper()
        elif ("read" in you) or ("new" in you):
            read_newspaper()
        elif "tell me" in you:
            tellabout()
        elif "youtube" in you:
            youtube() 
        elif "song" in you:
            song_youtube() 
        elif "open application" in you:
            open_application()
        elif "open webbsite" in you:
            open_webbsite()
        elif "day" in you or "now" in you:
            day()
        elif "time" in you:
            time_now()
        elif "location" in you:
            find_location()
        elif "bye" in you or "see you again" in you or "exit" in you:
            shield_brain("Goodbye Sir, See you again!")
            quit()
        else:
            db(you)
     
button_frame = Frame(window).pack(side=BOTTOM)
button_start = Button(button_frame, text="Start", width=15, font=(("Arial"), 10, "bold"), bg='#000000', fg='red', command=lambda: main())
button_start.place(x = 87, y = 483)
# button_pause = Button(button_frame, text="Pause", width=15, font=(("Arial"), 10, "bold"), bg='#000000', fg='red')
# button_pause.place(x = 320, y = 483)
button_exit = Button(button_frame, text="Exit", width=15, font=(("Arial"), 10, "bold"), bg='#000000', fg='red', command=window.quit)
button_exit.place(x = 550, y = 483)
window.mainloop()

import pyttsx3
import datetime, time
import speech_recognition as sr
import webbrowser as wb
import os          #cung cấp các chức năng được sử dụng để tương tác với hệ điều hành
import urllib      #dùng để mở các URL
import urllib.request as urllib2
import smtplib
import requests
import json     #Nội dung trong file json tồn tại theo cặp key: value. key là kiểu string, value thì có thể thuộc bất kỳ kiểu dữ liệu nào.
import re
import webbrowser
import ctypes   #ctypes là module dạng built-in cực mạnh của Python. Nó cho phép bạn sử dụng các lib sẵn có thừ một ngôn ngữ khác
import sys
import playsound
import wikipedia
import pywhatkit
import urllib
import simplejson
# import phonenumbers
# from phonenumbers import geocoder, carrier
from gtts import gTTS
from datetime import date
from selenium import webdriver
from youtube_search import YoutubeSearch
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import strftime
from validate_email import validate_email
from googlemaps import Client as GoogleMaps


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

def security_name():
    shield_brain("Welcome to the desktop virtual assistant: SHIELD.")   
    shield_brain("Please tell SHIELD your name!")
    while True:   
        name = shield_ear().title()
        if not name:
            shield_brain("SHIELD can't hear your name clearly.") 
            shield_brain("Please tell SHIELD your name again.")  
        else:
            shield_brain(f"Welcome {name} to SHIELD")
            break

def security_id():
    shield_brain("Please tell SHIELD your ID!")
    while True:
        id = shield_ear().title()
        if not id:
            shield_brain("Sorry! SHIELD cannot recognize your voice. Say ID again!") 
        elif ("1509" in id) or ("1999" in id):
            shield_brain("Correct ID!")
            break
        else:
            shield_brain(f"ID {id} is not correct, Please try another ID!")  

def greeting():
    hour = datetime.datetime.now().hour
    if hour < 11:
        shield_brain("Good morning, Sir! Wish you a good day.")
    elif hour < 13:
        shield_brain("Have you had lunch yet? Sir.")
    elif hour < 17:
        shield_brain("Good afternoon, Sir! Do you have any plans for this afternoon yet.")
    elif hour < 22:
        shield_brain("Good night, Sir! Have you had dinner yet.")
    else:
        shield_brain("Before you have a sweet dreams")
    shield_brain("How can i help you?")
    print("S.H.I.E.L.D: I'm listenning")
    print("S.H.I.E.L.D: ....")

def wikipedia1(text):
    wikipedia.set_lang("en")
    contents = wikipedia.summary(text).split("\n")
    shield_brain(wikipedia.summary(text, sentences=1))

def search1():
    shield_brain("What should SHIELD search, Sir?")
    while True:
        search = shield_ear().lower()
        if not search:
            shield_brain("SHIELD can't hear you clearly, can you repeat it?")
        else:
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            shield_brain(f"Here is what i found for {search} on Google")
            time.sleep(10)
            break
    shield_brain("What do you want SHIELD to do next?")

def search2(you):
    search = str(you).split("search" , 1)[1]
    url = f"https://www.google.com/search?q={search}"
    wb.get().open(url)
    shield_brain(f"Here is your {search} on Google")
    time.sleep(10)
    shield_brain("What do you want SHIELD to do next?")

def send_email():
    shield_brain("Who do you want to send Email to?")
    while True:
        name = shield_ear()
        if name:
            shield_brain(f"{name}'s email is:")
            while True:
                email = shield_ear().lower()
                if not email:
                    shield_brain(f"Please enter the Email you want to send to {name}: ")
                    email = input("")
                else:
                    pass
                regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"  # for custom mails use: "^[a-z0-9]+[\._]?[a-z0-9]+[@]
                if (re.search(regex,email)):        
                    pass
                    break
                else:
                    shield_brain("Wrong email! Please re-enter.")
            shield_brain("What do you want to send?")
            content = shield_ear().lower()
            if not content:
                content = input("The email content is: ")
            mail = smtplib.SMTP("smtp.gmail.com", 587)      #Máy chủ thư đi cổng 587 hỗ trợ TLS/STARTTLS
            mail.ehlo()
            mail.starttls()
            mail.login("thangndgch17549@fpt.edu.vn", "thang150907")
            mail.sendmail("thangndgch17549@fpt.edu.vn", email, content.encode('utf-8')) # Mã hóa để bảo mật mail
            mail.close()
            shield_brain("Your email has just been sent. Please check your email again!")
            time.sleep(10)
            break
        else:
            shield_brain("SHIELD don't understand who you want to email. Can you say it again?")
    shield_brain("What do you want SHIELD to do next?")    

def music():
    shield_brain("What number song do you want to hear?")
    music1 = r"C:\Users\nguye\OneDrive\Desktop\Project\movie&music\music1.mp4"
    music2 = r"C:\Users\nguye\OneDrive\Desktop\Project\movie&music\music2.mp4"
    music3 = r"C:\Users\nguye\OneDrive\Desktop\Project\movie&music\music3.mp4"
    music = shield_ear().lower()
    if "1" in music:
        os.startfile(music1)
        shield_brain("The song Forget someone who once loved by singer Chau Khai Phong was played.")
    elif "2" in music:
        os.startfile(music2)
        shield_brain("The song Ever Loved by singer Phan Duy Anh was played.")
    elif "3" in music:
        os.startfile(music3)
        shield_brain("The song April Is My Lie performed by singer Ha Anh Tuan was played.")
    else:
        os.startfile(music1)
        shield_brain("SHIELD can't hear you clearly, music 1 will be played")
    time.sleep(10)
    shield_brain("What do you want SHIELD to do next?")

def movie():
    shield_brain("What kind of movie would you like to watch?")
    action = r"C:\Users\nguye\OneDrive\Desktop\Project\movie&music\action.mp4"
    study = r"C:\Users\nguye\OneDrive\Desktop\Project\movie&music\study.mp4"
    funny = r"C:\Users\nguye\OneDrive\Desktop\Project\movie&music\funny.mp4"
    movie = shield_ear().lower()
    if "action" in movie:
        os.startfile(action)
        shield_brain("Action movie has been opened.")
    elif "study" in movie:
        os.startfile(study)
        shield_brain("Study movie has been opened.")
    elif "funny" in movie:
        os.startfile(funny)
        shield_brain("Funny movie has been opened.")
    else:
        os.startfile(funny)
        shield_brain("Sorry! SHIELD cannot recognize your voice. Funny movie has been opened.")
    time.sleep(15)
    shield_brain("What do you want SHIELD to do next?")    

def weather():
    result = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=f51a5b2b432b9d85d0aa3af4cf9eb2f1&q=hanoi&units=metric")
    data = result.json()  
    city_res = data["main"]
    current_temp = city_res["temp"]
    current_pres = city_res["pressure"]
    current_hum = city_res["humidity"]
    suntime = data["sys"]
    sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
    sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
    description = data["weather"]
    weather_des = description[0]["description"]
    now = datetime.datetime.now()

    weather = ("Today is {day} month {month} year {year}.\n".format(day = now.day, month = now.month, year= now.year) 
    + f"\tThe weather in Hà Nội city is: " + """
        The sun rises at {hourrise} hour {minrise} minute.
        The sun sets at {hourset} hour {minset} minute.
        Average temperature is {temp} °C.
        The air pressure is {pressure} hPa.
        Humidity is {humidity}%. 
        Today's sky is {weather_description}.
        Forecast scattered rain in several places.""".format(hourrise = sunrise.hour, minrise = sunrise.minute,
                                                            hourset = sunset.hour, minset = sunset.minute, 
                                                            temp = current_temp, pressure = current_pres, 
                                                            humidity = current_hum, weather_description = weather_des))
    shield_brain(weather)

    shield_brain("Would you like to know more weather elsewhere?")
    more = shield_ear().lower()
    if "yes" in more:
        shield_brain("What city would you like to see weather in?")
        web_url = "http://api.openweathermap.org/data/2.5/weather?"   # lưu đường đẫn đến api của trang web openweathermap.org 
        while True:
            city = shield_ear().title()
            if not city:
                shield_brain("SHIELD can't hear you clearly, can you repeat it?")
            else:
                api_key = "f51a5b2b432b9d85d0aa3af4cf9eb2f1"
                url = web_url + "appid=" + api_key + "&q=" + city + "&units=metric"
                result = requests.get(url)       # lấy thông tin truy vấn được từ trang web, lưu vào result
                data = result.json()                  # chuyển dữ liệu về kiểu json(sử dụng các cặp key - value để dữ liệu sử dụng)
                # print(data)
                if data["cod"] != "404":                # requests không bị lỗi
                    city_res = data["main"]
                    current_temp = city_res["temp"]
                    current_pres = city_res["pressure"]
                    current_hum = city_res["humidity"]
                    suntime = data["sys"]
                    sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
                    sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
                    description = data["weather"]
                    weather_des = description[0]["description"]
                    now = datetime.datetime.now()

                    weather = ("Today is {day} month {month} year {year}.\n".format(day = now.day, month = now.month, year= now.year) 
                    + f"\tThe weather in {city} is: " + """
                    The sun rises at {hourrise} hour {minrise} minute.
                    The sun sets at {hourset} hour {minset} minute.
                    Average temperature is {temp} °C.
                    The air pressure is {pressure} hPa.
                    Humidity is {humidity}%. 
                    Today's sky is {weather_description}.
                    Forecast scattered rain in several places.
                    """.format( hourrise = sunrise.hour, minrise = sunrise.minute,
                                hourset = sunset.hour, minset = sunset.minute, 
                                temp = current_temp, pressure = current_pres, 
                                humidity = current_hum, weather_description = weather_des))
                    shield_brain(weather)         
                    if current_temp <= 14:
                        shield_brain("When going out, remember to wear warm clothes!")
                    elif current_temp > 35:
                        shield_brain("It's sunny, remember to wear a hat when you go out!")
                    elif current_hum < 30:
                        shield_brain("The humidity is very low, remember to drink lots of water!")
                    else:
                        shield_brain("The weather is suitable for going out.")
                    time.sleep(5)
                    shield_brain("Do you want to know more weather in another area?")
                    another_city = shield_ear().title()
                    if "Yes" in another_city:
                        shield_brain("You want to know where the weather is?")                
                    else:
                        shield_brain("What do you want SHIELD to do next?")
                        break    
                else:
                    shield_brain("Your address could not be found")
                    shield_brain("Can you re-read where you want to see other weather?")
    else:
        shield_brain("What do you want SHIELD to do next?")

def change_wallpaper():
    api_key = "RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw"
    url = "https://api.unsplash.com/photos/random?client_id=" + \
        api_key                                                     # Lấy ảnh từ trang unspalsh.com
    while True:
        open = urllib2.urlopen(url)                                 # Mở đường dẫn url
        json_string = open.read()
        open.close()
        parsed_json = json.loads(json_string)
        photo = parsed_json["urls"]["full"]
        urllib2.urlretrieve(photo, "C:/Users/nguye/OneDrive/Desktop/Project/Image/a.png")   # địa chỉ lưu ảnh photo
        images=os.path.join("C:/Users/nguye/OneDrive/Desktop/Project/Image/a.png")
        ctypes.windll.user32.SystemParametersInfoW(20,0,images,3)
        shield_brain("Desktop wallpaper has just been changed, please check again.")
        time.sleep(2)
        shield_brain("Are you satisfied with the desktop wallpaper that has just been changed?")
        satisfied = shield_ear().lower()
        if "no" not in satisfied:
            break
    shield_brain("What do you want SHIELD to do next?") 

def read_newspaper():
    shield_brain("What newspaper do you want to read?")
    while True:
        news = shield_ear().lower()
        if not news:
            shield_brain("SHIELD can't hear clearly, can you say it again?")
        else:
            params = {"apiKey": "30d02d187f7140faacf9ccd27a1441ad", "q": news,}
            api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
            api_response = api_result.json()
            print("Newspaper: ")
            for number, result in enumerate(api_response["articles"], start=1):
                print(f"""New {number}:\nTitle: {result["title"]}\nQuote: {result["description"]}\nLink: {result["url"]} """)
                if number <= 3:
                    webbrowser.open(result["url"])
                    time.sleep(5)
            break 
    time.sleep(10)
    shield_brain("What do you want SHIELD to do next?")

def tellabout():
    shield_brain("What do you want to hear about?")
    while True:
        text = shield_ear().lower() 
        if not text:
            shield_brain("SHIELD can't hear clearly, can you say it again?")
        else:
            if "about" in text:
                text = str(text).split("about ", 1)[1]       
            try:
                wikipedia1(text)
                contents = wikipedia.summary(text).split("\n")
                for content in contents[1:]:
                    shield_brain("Do you want to hear more?")
                    answer = shield_ear().lower()
                    if "yes" not in answer:
                        break
                    shield_brain(content)
                shield_brain("Thank you for listening!")
                shield_brain("Would you like to ask anything else?")
                another_text = shield_ear().lower()
                if "yes" not in another_text:
                    break
                else:
                    shield_brain("What do you want to hear about?")
            except:
                shield_brain(f"Page id {text} does not match any pages. Try another id!") 
    time.sleep(5)
    shield_brain("What do you want SHIELD to do next?")

def youtube():
    shield_brain("What would you like to watch on YouTube?")
    while True:
        search = shield_ear().lower()
        if not search:
            shield_brain("Sorry! SHIELD cannot recognize your voice, can you say it again?")
        else:
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            shield_brain(f"Here is your {search} on Youtube") 
            break
    shield_brain("What do you want SHIELD to do next?")

def song_youtube():         
    while True:
        shield_brain("What song do you want to hear?")
        song = shield_ear().lower()
        if not song:
            shield_brain("Sorry! SHIELD cannot recognize your voice.")
        else:
            if "play" in song:
                song = song.replace("play", "")
            shield_brain(f"Please enjoy the song {song}. Press Enter to continue!")  
            pywhatkit.playonyt(song)
            if input("Press Enter to continue: ") != "":
                pass
            shield_brain("Do you want to listen to another song?")
            song_another = shield_ear().lower()
            if "yes" not in song_another:
                break           
    time.sleep(10)
    shield_brain("What do you want SHIELD to do next?")  

def open_webbsite(): 
    while True:
        shield_brain("Which website do you want to open?")
        web = shield_ear().lower().replace(" ", "")
        if not web:
            shield_brain("Sorry! SHIELD cannot recognize your voice, can you say it again?")
        elif "open" in web:
            web = web.split("open", 1)[1]
            if ".com" not in web:
                web = web + ".com"
        elif ".com" not in web:
            web = web + ".com"
        reg_ex = re.search("(.+)" ,web)
        # print(web)
        if reg_ex:
            domain = reg_ex.group(1)
            url = f"https://www." + domain
            # print(url)
            webbrowser.open(url)
            shield_brain("The web page you requested has been opened. Press Enter to continue!")
            if input("Press Enter to continue: ") != "":
                pass
            shield_brain("Would you like to open another website?")
            web_another = shield_ear().lower()
            if "yes" not in web_another:
                break
    time.sleep(5)
    shield_brain("What do you want SHIELD to do next?")

def open_application():
    shield_brain("What apps do you want me to open?")
    while True:
        open = shield_ear().lower()
        if not open:
            shield_brain("Sorry! SHIELD cannot recognize your voice, can you say it again?")
        elif "excel" in open:
            shield_brain("Open Microsoft Excel")
            os.system("C:\\Users\\nguye\\OneDrive\\Desktop\\Excel.lnk")
            break
        elif "word" in open:
            shield_brain("Open Microsoft Word")
            os.system("C:\\Users\\nguye\\OneDrive\\Desktop\\Word.lnk")
            break
        elif "google" in open or "chrome" in open:
            shield_brain("Open Google Chrome")
            os.system("C:\\Users\\nguye\\OneDrive\\Desktop\\Google Chrome.lnk") 
            break
        elif "notepad" in open:
            shield_brain("Open Notepad")
            os.system("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk") 
            break
        else:
            shield_brain("Application not installed. Please try again!")
    shield_brain("What do you want SHIELD to do next?")
def day():
    Day = datetime.date.today().strftime("Today is: %B %d, %Y")
    shield_brain(Day)

def time_now():
    Time = datetime.datetime.now().strftime("The time now is: %H hours %M minutes %S seconds")
    shield_brain(Time)

def find_location():
    while True:
        shield_brain("What is the location?")
        location = shield_ear()
        if not location:
            shield_brain("SHIELD can't hear you clearly, can you repeat it?")
        else:
            url = "https://google.nl/maps/place/" + location + "/&amp;"
            webbrowser.get().open(url)
            shield_brain(f"Here is the location of {location}.")
            time.sleep(3)
            shield_brain("Do you want to find another location?")
            answer = shield_ear().lower()
            if "yes" not in answer:
                print("Boss: ...")   
                break                     
    time.sleep(10)    
    shield_brain("What do you want SHIELD to do next?")














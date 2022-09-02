    import speech_recognition as sr
    import pyttsx3
    import pywhatkit
    import datetime
    import wikipedia as w
    import sched
    import flask
    import subprocess
    import cv2
    import tkinter
    import json
    import random
    import operator
    import webbrowser
    import os
    import winshell
    import pyjokes
    import feedparser
    import smtplib
    import ctypes
    import time
    import requests
    import shutil
    from bs4 import BeautifulSoup
    from twilio.rest import Client
    from clint.textui import progress
    from ecapture import ecapture as ec
    from bs4 import BeautifulSoup
    from translate import Translator
    import keyboard
    from keyboard import press
    from keyboard import write
    import win32com.client as wincl
    from urllib.request import urlopen
    
    #todo----This is the voice of "Jarvis" :-()
    
    listner = sr.Recognizer()
    engine = pyttsx3.init()
    voices =  engine.getProperty('voices')
    audio = pyttsx3.init()
    audio.setProperty('rate',142)
    audio.setProperty('volume',7.0)
    engine.setProperty('voice',voices[0].id)
    
    #todo-------this function voice of jarvis
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    
    #todo------window_shortcuts
    
    def change_window():
        audio.say('sure')
        audio.runAndWait()
        keyboard.press_and_release('alt+tab')
    
    def home():
        audio.say('okay')
        audio.runAndWait()
        keyboard.press_and_release('windows+d')
    
    def close():
        audio.say('okay')
        audio.runAndWait()
        keyboard.send('alt+F4','space')
    
    def username():
        audio.say("What should i call you sir")
        audio.runAndWait()
        uname = take_command()
        audio.say(f"Welcome Mister{uname}")
        audio.runAndWait()
    
    #todo--------This command take command and recognize
    
    def take_command():
        with sr.Microphone() as source:
            print("listning.....")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            print(command)
        return command
    
    #todo------- translate
    def translate():
        audio.say('what you want to translate')
        audio.runAndWait()
        tr = take_command()
        translator = Translator(from_lang="english", to_lang="hindi")
        translation = translator.translate(tr)
        audio.say('Here is your translate')
        audio.runAndWait()
        print(translation)
    
    #todo----------This function for constantly awake jarvis
    schedulerTest = sched.scheduler(time.time, time.sleep)
    
    def wakeup(test = 'default'):
        print("Testing Scheduler to Run Script Constantly.")
        schedulerTest.enter(0, 1, wakeup, ('checkThis',))
        while True:
            try:
                command = take_command()
                print('....',command)
                if "jarvis" in command:
                    username()
                    wishMe()
    
                elif command == 0:
                    continue
    
                elif "stop" in command or "exit" in command or "goodbye" in command:
                    speak("Ok bye and take care")
                    print("Ok bye and take care")
                    break
                elif 'play' in command:
                    song = command.replace('play', '')
                    audio.say('OK sir as per your wish playing' + song)
                    audio.runAndWait()
                    pywhatkit.playonyt(song)
    
                elif "what's your name" in command or "What is your name" in command:
                    audio.say("You call me jarvis and i like this name")
                    audio.runAndWait()
    
                elif 'time' in command:
    
                    timee = date_time()
                    audio.say(f"Sir it's {timee}")
                    audio.runAndWait()
                    print(timee)
    
                elif 'good morning' in command or 'good afternoon' in command or 'good evening' in command:
                    hour = int(datetime.datetime.now().hour)
                    if hour >= 0 and hour < 12:
                        audio.say("Hello sir!Good Morning !")
                        audio.runAndWait()
                    elif hour >= 12 and hour < 18:
                        audio.say("Hello sir!Good Afternoon !")
                        audio.runAndWait()
                    else:
                        audio.say("Hello sir!Good Evening !")
                        audio.runAndWait()
    
                elif "advice" in command:
                    speak(f"Here's an advice for you, sir")
                    advice = get_random_advice()
                    speak(advice)
                    speak("For your convenience, I am printing it on the screen sir.")
                    print(advice)
    
                elif 'how are you' in command or 'how are you jarvis' in command:
                    greetings = ["Hi, sir i am fine.", "hi, i am so fine sir.", "i am great as ever.","i am good."]
                    jquest = ["what about you sir.", "how are you sir.","how's the day sir","how have you been, sir."]
                    greeting = random.choice(greetings)
                    audio.say(greeting)
                    jquesti = random.choice(jquest)
                    audio.say(jquesti)
                    audio.runAndWait()
                    chat = take_command()
                    if 'not fine' in chat:
                        audio.say("what's happen sir, i am here for make your day.")
                        audio.say("What can i do for you, sir?")
                        audio.runAndWait()
    
                        chat = take_command()
                        if 'play' in chat:
                            song = command.replace('play', '')
                            audio.say('OK sir as per your wish playing' + song)
                            audio.runAndWait()
                            pywhatkit.playonyt(song)
                        elif 'joke' in chat:
                            jokes()
                    elif 'fine' in chat or 'good' in chat or 'pretty good' in chat:
                        audio.say("Great sir.")
                        audio.say("lets do something new today")
                        audio.runAndWait()
    
                elif 'what is' in command or 'who is' in command:
                    person = command.replace('who is', '')
                    pywhatkit.search(person)
                    r = w.summary(person, 1)
                    audio.say(r)
                    audio.runAndWait()
    
                elif 'set reminder' in command:
                    speak("What shall I remind you about?")
                    text = take_command()
                    speak("In how many minutes?")
                    local_time = take_command()
                    local_time = int(local_time) * 60
                    time.sleep(local_time)
                    speak(f"sir this is reminder for {text}")
    
                elif 'remember' in command:
                    keepnote()
                    audio.say("What should i write, sir")
                    audio.runAndWait()
                    note = take_command()
                    file = open('notes.txt', 'a+')
                    audio.say("Sir, Should i include date and time")
                    audio.runAndWait()
                    snfm = take_command()
                    if 'yes' in snfm or 'sure' in snfm:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        file.write(strTime)
                        file.write(" :- ")
                        file.write(note+"\n")
                    else:
                        file.write(note+"\n")
                elif 'send a mail' in command:
                    try:
                        audio.say("What should I say?")
                        audio.runAndWait()
                        content = take_command()
                        audio.say("whome should i send")
                        audio.runAndWait()
                        to = input()
                        sendEmail(to, content)
                        audio.say("Email has been sent !")
                        audio.runAndWait()
                    except Exception as e:
                        print(e)
                        audio.say("sorry sir I am not able to send this email")
                        audio.runAndWait()
    
                elif 'open youtube' in command:
                    audio.say("Here you go to Youtube\n")
                    audio.runAndWait()
                    webbrowser.open("https://www.youtube.com/")
    
                elif 'open google' in command:
                    audio.say("Here you go to Google\n")
                    audio.runAndWait()
                    webbrowser.open("https://www.google.com/")
    
                elif 'open whatsapp' in command:
                    audio.say("Here you go to whatsapp\n")
                    audio.runAndWait()
                    webbrowser.open("https://web.whatsapp.com/")
                elif 'send message' in command:
                    pywhatkit.sendwhatmsg("+91 9744929392","Hello i am ss killer",12,45)
    
                elif 'translate' in command:
                    translate()
    
                elif 'openstack overflow' in command or 'open stack overflow' in command:
                    audio.say("Here you go to Stack Over flow.Happy coding")
                    audio.runAndWait()
                    webbrowser.open("https://stackoverflow.com/")
    
                elif 'lock window' in command:
                    audio.say("locking the device")
                    audio.runAndWait()
                    ctypes.windll.user32.LockWorkStation()
    
                elif 'shutdown system' in command:
                    audio.say("Hold On a Sec ! Your system is on its way to shut down")
                    audio.runAndWait()
                    subprocess.call('shutdown /s /t 1')
    
                elif "camera" in command:
                    audio.say("Hold On a Second ! Camera is opening")
                    audio.runAndWait()
                    os.system("start microsoft.windows.camera:")
    
                elif "take a photo" in command:
                    audio.say("Ready? say cheez")
                    audio.runAndWait()
                    videoCaptureObject = cv2.VideoCapture(0)
                    result = True
                    while (result):
                        ret, frame = videoCaptureObject.read()
                        cv2.imwrite("NewPicture.jpg", frame)
                        result = False
                    videoCaptureObject.release()
                    cv2.destroyAllWindows()
                elif "friend" in command or "friends" in command:
                    audio.say("yes ,i know your some friends")
                    audio.runAndWait()
                    friend = take_command()
                    if 'brothers' in friend or "brother" in friend:
                        audio.say('''Definitely i know N B brothers are new era of this music industry , The name of singer from the band is ss killer and adun
                        They both are have uniqe voice. They have some own composotions like In-Aankho, jhaha mera, chhaahat but , my personal fav is in aankho.
                        ''')
                        audio.runAndWait()
    
                    elif 'rakesh' in friend or 'raklo' in friend:
                        audio.say('''How forgot this person. this is one and only your best friend.
                         you both are amazing togather.
                         ''')
                        audio.say('look i wish you guys are always be togather')
                        audio.say('you guys are very creative and i am also your creativity.')
                        audio.say('I hope you will do something big which never done by anyone')
                        audio.runAndWait()
    
                    elif 'sourav' in friend:
                        audio.say('''he is your best friend .
                         ''')
                        audio.say('you both have same name thats why power of s s name is cool for you')
                        audio.say('you think many plans to gather and you will do for sure')
                        audio.runAndWait()
    
                elif 'create folder' in command:
                    audio.say('what should i name the folder?')
                    audio.runAndWait()
                    folder = take_command()
                    newpath = r'E:' '/'+folder
                    if not os.path.exists(newpath):
                        os.makedirs(newpath)
                    audio.say(f'{folder} folder created')
                    audio.runAndWait()
    
                elif 'is love' in command:
                    audio.say("It is 7th sense that destroy all other senses")
                    audio.runAndWait()
    
                elif "who are you" in command:
                    audio.say("I am your virtual assistant created by Mr.s s killer")
                    audio.runAndWait()
    
                elif "don't listen" in command:
                    audio.say("for how much time you want to stop jarvis from listening commands")
                    audio.runAndWait()
                    a = int(take_command())
                    audio.say("i am sleeping")
                    audio.runAndWait()
                    time.sleep(a)
                    audio.say("Hello sir i am back")
                    audio.runAndWait()
    
    
                elif "restart" in command:
                    audio.say("Hold On a Sec ! Your system is on its way to restart")
                    audio.runAndWait()
                    subprocess.call(["shutdown", "/r"])
    
                elif "who i am" in command:
                    audio.say("If you talk then definitely your human.")
                    audio.runAndWait()
    
                elif "why you came to world" in command:
                    audio.say("Thanks to the man ... further It's a secret")
                    audio.runAndWait()
    
                elif 'open vs code' in command:
                    audio.say("opening v s code")
                    audio.runAndWait()
                    os.popen(r"E:\Visual Studio Code.lnk")
    
                elif 'open pycharm' in command:
                    audio.say("opening pycharm")
                    audio.runAndWait()
                    os.popen(r"E:\PyCharm Community Edition 2022.1.3.lnk")
    
                elif 'change window' in command:
                    change_window()
    
                elif 'home' in command:
                    home()
    
                elif 'close' in command:
                    close()
    
                else:
                    # audio.say("im not your assistant")
                    # audio.runAndWait()
                    # print("im not your assistant")
                    continue
            except:
                take_command()
    
    #todo----sendmail
    
    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
    
        # Enable low security in gmail
        server.login('your email id', 'your email password')
        server.sendmail('your email id', to, content)
        server.close()
    
    #todo----wishme as time
    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            audio.say("Hello sir!Good Morning !")
    
        elif hour >= 12 and hour < 18:
            audio.say("Hello sir!Good Afternoon !")
    
        else:
            audio.say("Hello sir!Good Evening !")
        time = date_time()
        w = weather()
        Temp = w[0]
        Temp = Temp.replace('c','celcius')
        sky = w[1]
        audio.say(f"Sir it's {time}")
        audio.say(f"the temperature is {Temp}")
        audio.say(f"and Todays oytside weather will be {sky}")
        audio.say("I am your Jarvis!how can i help you?")
        audio.runAndWait()
    
    #todo----Random advise
    
    def get_random_advice():
        res = requests.get("https://api.adviceslip.com/advice").json()
        return res['slip']['advice']
    
    #todo----tell me about weather
    def weather():
        # enter city name
        r = requests.get('https://ipinfo.io/')
        data = r.json()
        c = data['city']
        city = c
    
        # create url
        url = "https://www.google.com/search?q=" + "weather" + city
    
        # requests instance
        html = requests.get(url).content
    
        # getting raw data
        soup = BeautifulSoup(html, 'html.parser')
    
        # get the temperature
        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    
        # this contains time and sky description
        str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    
        # format the data
        data = str.split('\n')
        time = data[0]
        sky = data[1]
    
        # list having all div tags having particular clas sname
        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    
        # particular list with required data
        strd = listdiv[5].text
    
        # formatting the string
        pos = strd.find('Wind')
        other_data = strd[pos:]
        return temp,sky
    
    #todo------tell me about time
    def date_time():
        time = datetime.datetime.now().strftime('%I:%M %p')
        return time
    
    #todo------Pyjoke
    def jokes():
        My_joke = pyjokes.get_joke(language="en", category="neutral")
        print(My_joke)
        audio.say(My_joke)
        audio.runAndWait()
        return My_joke
    
    #todo-------Notes
    def keepnote():
        with open("notes.txt","a") as f:
            # f.write("")
            f.close()
    
    #todo--------Here is call the function for awake jarvis constantly.
    
    schedulerTest.enter(0, 1, wakeup, ('TestThis',))
    schedulerTest.run()

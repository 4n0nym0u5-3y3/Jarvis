import os
import sys
import time
from PyDictionary import PyDictionary as Diction
import keyboard
import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import pyjokes
import datetime
from playsound import playsound
import psutil
import platform
from time import sleep
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Mark2 import Ui_MainWindow
import PyPDF2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 170)




def speak(audio):
    print("  ")
    print(f": {audio} ")
    print("  ")
    engine.say(audio)
    engine.runAndWait()

    def takecommand(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:

            print("Listening....")

            r.pause_threshold = 1

            audio = r.listen(source)

        try:

            print("Recognizing....")

            query = r.recognize_google(audio, language='en-in')

            print(f": your command : {query}\n")

        except Exception as Error:

            return "none"

        return query.lower()


def speak(audio):
    print("  ")
    print(f": {audio} ")
    print("  ")
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    timee = time.strftime("%I:%M %p")
    if (hour > 0 and hour <= 12):
        speak(f"Good morning sir its {timee}")
    elif (hour > 12 and hour < 18):
        speak(f"Good afternoon sir its {timee}")
    else:
        speak(f"Good evening sir its {timee}")
    speak("Your assistant Jarvis at your service sir...How can I help you")


def pdf_reader():
    speak("Sir can u please enter the correct file location of the pdf u need me to read out please")
    pdflocation = input()
    book = open(pdflocation, 'rb')
    pdfreader = PyPDF2.PdfFileReader(book)
    pagecount = pdfreader.numPages
    speak(f"Sir there are totally {pagecount} pages in the book u told me to read sir")
    speak("Sir please enter the page number of the book u need me to read ")
    pagenumber = int(input("Enter the page number sir: "))
    page = pdfreader.getPage(pagenumber)
    contents = page.extractText()
    speak(contents)


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.taskexe()

    def takecommand(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:

            print("Listening....")

            r.pause_threshold = 1

            audio = r.listen(source)

        try:

            print("Recognizing....")

            query = r.recognize_google(audio, language='en-in')

            print(f": your command : {query}\n")

        except Exception as Error:

            return "none"

        return query.lower()

    def taskexe(self):
        def openapps():
            self.query = self.takecommand()
            speak("Ok sir, wait a second")

            if 'visual code' in self.query:
                os.startfile("C:\\Users\\uppal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

            elif 'kali linux' in self.query:
                os.startfile("C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe")

            elif 'minecraft' in self.query:
                os.startfile("C:\\Users\\uppal\\AppData\\Roaming\\.minecraft\\TLauncher.exe")

            elif 'google' in self.query:
                os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

            elif 'youtube' in self.query:
                webbrowser.open("https://www.youtube.com")

            speak("Your command has been completed sir")

        def closeapp():
            self.query = self.takecommand()
            speak("Ok sir, wait a second!")

            if "youtube" in self.query:
                os.system("TASKKILL /F /im msedge.exe ")

            elif "google" in self.query:
                os.system("TASKKILL /F /im msedge.exe ")

            elif "minecraft" in self.query:
                os.system("TASKKILL /F /im TLauncher.exe ")

            elif "kali linux" in self.query:
                os.system("TASKKILL /F /im VirtualBox.exe")

            elif "visual code" in self.query:
                os.system("TASKKILL /F /im msedge.exe ")

            speak("Your command has been completed sir")

        def youtubeauto():
            speak("Whats your command ?")
            comm = self.takecommand()

            if 'pause' in comm:
                keyboard.press('space bar')

            elif 'restart' in comm:
                keyboard.press('0')

            elif 'mute' in comm:
                keyboard.press('m')

            elif 'restart' in comm:
                keyboard.press('0')

            elif 'skip' in comm:
                keyboard.press('l')

            elif 'back' in comm:
                keyboard.press('j')

            elif 'full screen' in comm:
                keyboard.press('f')

            elif 'film mode' in comm:
                keyboard.press('t')

            speak("Done sir")

        def dictionary():
            speak("Activating dictionary")
            speak("Tell me the problem sir !")
            prob1 = self.takecommand()

            if 'meaning' in prob1:
                prob1 = prob1.replace("what is the", " ")
                prob1 = prob1.replace("meaning of", " ")
                prob1 = prob1.replace("jarvis", " ")
                result = Diction.meaning(prob1)
                speak(f"The meaning of {prob1} is {result}")

            elif "synonym" in prob1:
                prob1 = prob1.replace("what is the", " ")
                prob1 = prob1.replace("synonym of", " ")
                prob1 = prob1.replace("jarvis", " ")
                result = Diction.synonym(prob1)
                speak(f"The synonym of {prob1} is {result}")

            elif "antonym" in prob1:
                prob1 = prob1.replace("what is the", " ")
                prob1 = prob1.replace("antonym of", " ")
                prob1 = prob1.replace("jarvis", " ")
                result = Diction.antonym(prob1)
                speak(f"The antonym of {prob1} is {result}")

            speak("Exiting dictionary !")

        def news():
            news_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3d7d2570874a4de697f837fc650bb57b"
            news_page = requests.get(news_url).json()
            articles = news_page["articles"]
            headlines = []
            days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
            for a in articles:
                headlines.append(a["title"])
            for i in range(len(days)):
                speak(f"Today's {days[i]}  news is: {headlines[i]}")

        def pdf_reader():
            speak("Sir can u please enter the correct file location of the pdf u need me to read out please")
            pdflocation = input()
            book = open(pdflocation, 'rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pagecount = pdfreader.numPages
            speak(f"Sir there are totally {pagecount} pages in the book u told me to read sir")
            speak("Sir please enter the page number of the book u need me to read ")
            pagenumber = int(input("Enter the page number sir: "))
            page = pdfreader.getPage(pagenumber)
            contents = page.extractText()
            speak(contents)

        wish()
        while True:

            self.query = self.takecommand().lower()

            if 'hello jarvis' in self.query:
                speak("Hello sir, I am jarvis ")
                speak("your personal AI assistant")
                speak("How can i help you? ")

            elif 'hey jarvis how are you' in self.query:
                speak("I am fine sir !")
                speak("What about you?")

            elif 'i am fine' in self.query:
                speak("That's nice to here")
                speak("So whats the new plans for today?")

            elif 'i think you need a break' in self.query:
                speak("Ok Sir, you can call me any time")
                break

            elif 'bye jarvis' in self.query:
                speak("bye sir")
                break

            elif 'jarvis do youtube search of' in self.query:
                speak("Ok sir, this is what i found for your search")
                self.query = self.query.replace("jarvis", " ")
                self.query = self.query.replace("do youtube search of", " ")
                web = "https://www.youtube.com/results?search_query=" + self.query
                webbrowser.open(web)
                speak("Done sir")

            elif 'jarvis do google search' in self.query:
                speak("This is what i found for your search sir")
                self.query = self.query.replace("jarvis", " ")
                self.query = self.query.replace("do google search", " ")
                pywhatkit.search(self.query)
                speak("Done sir")

            elif 'jarvis launch website' in self.query:
                speak("Tell me the name of the website")
                name = self.takecommand()
                web1 = 'https://www.' + name + '.com'
                webbrowser.open(web1)
                speak("launched!")

            elif 'jarvis search on wikipedia' in self.query:
                speak("Searching wikipedia....")
                self.query = self.query.replace("jarvis", " ")
                self.query = self.query.replace("search on wikipedia", " ")
                wiki = wikipedia.summary(self.query, 2)
                speak(f"According  to wikipedia : {wiki}")

            elif 'jarvis where i am' in self.query or 'jarvis where we are' in self.query:
                speak('wait sir, let me check')
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    region = geo_data['region']
                    country = geo_data['country']
                    speak(f"sir i am not sure, but i think we are in {region} region of {city} city of {country} country")

                except Exception as e:
                    speak("sorry sir, due to network issue i am not able to find where we are")

            elif 'take screenshot' in self.query or 'take a screenshot' in self.query:
                speak("sir, please tell me the name for this screenshot file ")
                name = self.takecommand().lower()
                speak("please sir hold the screen for few seconds, i am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done sir, ")

            elif 'open visual code' in self.query:
                openapps()

            elif 'open kali linux' in self.query:
                openapps()

            elif 'open minecraft' in self.query:
                openapps()

            elif 'open google' in self.query:
                openapps()

            elif 'open youtube' in self.query:
                openapps()

            elif 'close visual code' in self.query:
                closeapp()

            elif 'close kali linux' in self.query:
                closeapp()

            elif 'close minecraft' in self.query:
                closeapp()

            elif 'close google' in self.query:
                closeapp()

            elif 'close youtube' in self.query:
                closeapp()

            elif 'pause' in self.query:
                youtubeauto()

            elif 'restart' in self.query:
                youtubeauto()

            elif 'mute' in self.query:
                youtubeauto()

            elif 'restart' in self.query:
                youtubeauto()

            elif 'skip' in self.query:
                youtubeauto()

            elif 'back' in self.query:
                youtubeauto()

            elif 'full screen' in self.query:
                youtubeauto()

            elif 'film mode' in self.query:
                youtubeauto()

            elif 'jarvis tell me a joke' in self.query:
                get = pyjokes.get_joke()
                speak(get)

            elif 'jarvis open dictionary' in self.query:
                dictionary()

            elif "what is my ip address" in self.query:
                ip = requests.get("https://api.ipify.org").text
                speak(f"Sir your ip address is: {ip}")

            elif "tell me the cpu information" in self.query:
                speak(f"Physical cores:{psutil.cpu_count(logical=False)}")
                speak(f"Total cores:{psutil.cpu_count(logical=True)}")
                cpufreq = psutil.cpu_freq()
                speak(f"Max Frequency: {cpufreq.max:.2f}Mhz")
                speak(f"Min Frequency: {cpufreq.min:.2f}Mhz")
                speak(f"Current Frequency: {cpufreq.current:.2f}Mhz")
                speak("CPU Usage Per Core:")
                for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                    speak(f"Core {i}: {percentage}%")
                speak(f"Total CPU Usage: {psutil.cpu_percent()}%")

            elif "tell me the battery information" in self.query:
                speak(f"Sir you have used {psutil.sensors_battery()} percentage of battery")

            elif "ram usage" in self.query:
                psutil.cpu_percent()
                psutil.virtual_memory()
                dict(psutil.virtual_memory()._asdict())
                speak(f"Sir you have used {psutil.virtual_memory().percent} percentage of RAM")

            elif "memory available" in self.query:
                psutil.cpu_percent()
                psutil.virtual_memory()
                dict(psutil.virtual_memory()._asdict())
                speak(
                    f"Sir your available memory is: {int(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)} percentage")

            elif "jarvis tell me the news" in self.query:
                speak("Just give me a moment fetching some top headlines for you......")
                news()

            elif "tell me about system information" in self.query:
                uname = platform.uname()
                speak(f"System: {uname.system}")
                speak(f"Node Name: {uname.node}")
                speak(f"Release: {uname.release}")
                speak(f"Version: {uname.version}")
                speak(f"Machine: {uname.machine}")
                speak(f"Processor: {uname.processor}")

            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                sleep(1)
                pyautogui.keyUp("alt")

            elif "jarvis play song in youtube" in self.query:
                speak("Sir, what song do you want me to play on youtube")
                songcommand = input("Enter the name of song : ")
                pywhatkit.playonyt(f"{songcommand}")

            elif "memory information" in self.query:
                def get_size(bytes, suffix="B"):
                    factor = 1024
                    for unit in ["", "K", "M", "G", "T", "P"]:
                        if bytes < factor:
                            return f"{bytes:.2f}{unit}{suffix}"
                        bytes /= factor
                    return bytes

                speak("Sir your memory information:")
                # get the memory details
                svmem = psutil.virtual_memory()
                speak(f"Total: {get_size(svmem.total)}")
                speak(f"Available: {get_size(svmem.available)}")
                speak(f"Used: {get_size(svmem.used)}")
                speak(f"Percentage: {svmem.percent}%")
                speak("Swap Memory")
                # get the swap memory details (if exists)
                swap = psutil.swap_memory()
                speak(f"Total: {get_size(swap.total)}")
                speak(f"Free: {get_size(swap.free)}")
                speak(f"Used: {get_size(swap.used)}")
                speak(f"Percentage: {swap.percent}%")

            elif "read pdf" in self.query:
                pdf_reader()


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../../Downloads/1x0k0Fl.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("../../Downloads/Code_Template.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("../../Downloads/Earth_Template.gif")
        self.ui.label_9.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("../../Downloads/initial.gif")
        self.ui.label_10.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("../../Downloads/8871.gif")
        self.ui.label_11.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("../../Downloads/RE2QPxN.gif")
        self.ui.label_12.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("../../Downloads/solar-system-11.gif")
        self.ui.label_13.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("../../Downloads/igD3dpj.gif")
        self.ui.label_14.setMovie(self.ui.movie)
        self.ui.movie.start()

        startExecution.start()


app = QApplication(sys.argv)
jarvis2 = Main()
jarvis2.show()
exit(app.exec_())

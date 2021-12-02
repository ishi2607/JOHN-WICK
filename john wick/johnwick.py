import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyautogui
# import smtplib
import pyjokes
import cv2
import screenshot
#import weather_app
import pywhatkit as kit
def rootn():
    screenshot.takeScreenshot()


# def canvas1():
#     weather_app.canvas.mainloop()




engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
# print(voices[1].id) #ye dekhne ke liye thi iska use nahi
engine.setProperty('voices', voices[1].id)


#ye function bulaane se voh bolega
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#yeh function se voh apne ko wish karega, i.e. good morning good afternoon acording to time
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")

    else:
        print("Good Evening!")
        speak("Good Evening!")

    print("I'm John Wick, how can I help you?")    
    speak("I'm John Wick, how can I help you?")    



#is function se baat sunega 
def takeCommand():
    #takes microphone input aur output string form me deta hai

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source) 

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #speak("Say that again please")
       # print(e) #isse error print hoga, jo recognizer nahi hua
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query



# '''def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password') #yahan gmail id aur pass daalna apna
#     server.sendmail('youremail@gmail.com',to,content)
#     server.close() '''



if __name__=="__main__":
    print("Hello There!!")
    speak("Hello There!!")
    wishMe()
    while True:
        query= takeCommand().lower()  #yaha pe lower() likhna galti se bhi mat hota nahi toh iterable error dega i.e loop nahi chalega, also lowercase nahi kiya toh bau hojayegi
        #logic for excuting tasks based on query
        if 'open youtube' in query:
            webbrowser.open("youtube.com")


        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results) 

        elif 'tell us about yourself' in query:
            print("Well, I'm john wick. I am an AI based desktop assistant. I help people making their PC experience better. I was developed By Guneet, Ishita and mayank for their third year minor project. Also i'm smarter than anyone in this room, and my creaters are fabulous")
            speak("Well, I'm john wick. I am an AI based desktop assistant. I help people making their PC experience better. I was developed By Guneet, Ishita and mayank for their third year minor project. Also i'm smarter than anyone in this room, and my creaters are fabulous")

        elif   'open google' in query:              #internet explorer me kholega
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:        #internet explorer me kholega
            webbrowser.open("stackoverflow.com")    

        elif 'send a whatsapp message' in query:
            speak("Please enter the no. to message:")
            no_to_msg=input("Please enter the number to message:")
            speak("Enter the msg to send:")
            msg_to_send=input("Enter the msg to send:")
            print("Enter the time to send msg:")
            speak("Enter the time to send msg in 24 hour format:")
            hr_for_msg=int(input())
            min_for_msg=int(input())
            kit.sendwhatmsg(f"{no_to_msg}",f"{msg_to_send}",hr_for_msg,min_for_msg)
            speak("You msg delivery time details are displayed")

        elif 'play music' in query:
            music_dir =  'C:\\MYMUSIC' 
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0])) 

        elif 'tell the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"{strTime}")
            speak(f"The time is {strTime}")

        elif 'open vs code' in query:
            codePath =  "C:\\VS CODE\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)  #codepath me jo path doge wahi file kholega
        
        elif 'open pycharm' in query:
            codePath =  "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.1\\bin\\pycharm64.exe"
            os.startfile(codePath)  #codepath me jo path doge wahi file kholega

        elif 'open code blocks' in query:
            codePath =  "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
            os.startfile(codePath)  #codepath me jo path doge wahi file kholega

        elif 'open sublime text' in query:
            codePath =  "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(codePath)  #codepath me jo path doge wahi file kholega        
    
        elif 'open discord' in query:
            codePath =  "C:\\Users\\gunee\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe"
            os.startfile(codePath) 
        
        elif 'open spotify' in query:
            codePath = "C:\\Users\\gunee\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath)
        
        # elif 'close spotify' in query:
        #     os.system("taskkill /Spotify.exe")
            
       
        elif 'open teams' in query:
            codePath = "C:\\Users\\gunee\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
            os.startfile(codePath)    

        elif 'open steam' in query:
            codePath = "C:\\Program Files (x86)\\Steam\\steam.exe"
            os.startfile(codePath)

        elif 'open photoshop' in query:
            codePath = "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"
            os.startfile(codePath)    

        elif 'open filmora' in query:
            codePath = "C:\\Program Files\\Wondershare\\Wondershare Filmora\\Wondershare Filmora X.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            codePath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)


        elif 'open epic games' in query:
            codePath="C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\EpicGamesLauncher.exe"
            os.startfile(codePath)

        elif 'open postman'  in query:
            codePath="C:\\Users\\gunee\\AppData\\Local\\Postman\\Postman.exe"
            os.startfile(codePath)


        elif 'open android studio'  in query:
            codePath="C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(codePath)    

        elif 'open webex' in query:
            codePath="C:\\Users\\gunee\\AppData\Local\\Programs\\Cisco Spark\\CiscoCollabHost.exe"
            os.startfile(codePath)

        elif 'open GeForce experience' in query:                  #caps ke kaaran nahi chalra i guess
            codePath="C:\\Program Files\\NVIDIA Corporation\\NVIDIA GeForce Experience\\NVIDIA GeForce Experience.exe"
            os.startfile(codePath)

        elif 'open winrar' in query:
            codePath="C:\\Program Files\\WinRAR\\WinRAR.exe"
            os.startfile(codePath)    
            
        elif 'open xm' in query:
            codePath="C:\\xampp\\xampp-control.exe"
            os.startfile(codePath)       
        
        elif 'open tor' in query:
            codePath="C:\\Users\\gunee\\Desktop\\Tor Browser\\Browser\\firefox.exe"
            os.startfile(codePath)
        
        elif 'open excel' in query:
            codePath="C: \\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.exe"
            os.startfile(codePath)

        elif 'open word' in query:
            codePath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe"
            os.startfile(codePath)

        elif 'open powerpoint' in query:
            codePath="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.exe"
            os.startfile(codePath)

        elif 'open command prompt' in query:
            codePath="C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(codePath)

        elif 'open downloads' in query:                
            codePath="C:\\Users\\gunee\\Downloads" 
            os.startfile(codePath)   

        elif 'open files' in query:                
            codePath="C:\\" 
            os.startfile(codePath)

        elif 'open settings' in query:                
            codePath="C:\\WINDOWS\\System32\\Control.exe" 
            os.startfile(codePath)
                
        # elif 'close setting' in query:                
        #         codePath="C:\\WINDOWS\\System32\\Control.exe"   #close karne ka try kar raha tha file
        #         os.close(codePath)


        elif 'open zoom' in query:                
            codePath="C:\\Users\\gunee\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe" 
            os.startfile(codePath)

        # elif 'open weather app' in query:                
        #     canvas1()

        elif 'take screenshot' in query:                
            rootn()

        elif 'tell a joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())

        elif 'increase volume' in query:
            pyautogui.press("volumeup")

        elif 'decrease volume' in query:
            pyautogui.press("volumedown")

        elif 'mute' in query:
            pyautogui.press("volumemute")
        
        elif 'light' in query:
            pyautogui.press("brightnessup")
            
        elif 'open camera' in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitkey(50)
                if k==27:
                    break;
            cap.release()        
            cv2.destroyAllWindows()


        # elif 'email to guneet' in query: #email function still in process, therefore yeh chalega nahi.
        #     try:
        #         speak("What should I say")
        #         content = takeCommand()
        #         to = "gunit100001@gmail.com"
        #         sendEmail(to,content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry could not send this email")     
        
        elif 'sing a song'in query:
            print("No")
            speak("No")

        elif 'what the hell man' in query:
            print("What? Its my favorite song")
            speak("What? Its my favorite song")

        elif 'please'in query:
            print("All right here goes nothing.....")
            speak("All right here goes nothing.....")
            speak("aaaaaaaaaaaaaaaaaaaaaaaaaa, sorry i can't sing")
            print("sorry, i can't sing")

        elif 'so sweet' in query:
            print("ewwww 10 feet duur reh ")
            speak("ewwww 10 feet duur reh ")


        elif 'thank you' in query:
            print("No problem, do you need any further help?")
            speak("No problem, do you need any further help?")

        elif ('quit' or "that's all") in query:
            print("Thank you for using me, have a great day!")
            speak("Thank you for using me, have a great day!")
            exit()               

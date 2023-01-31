import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
from tkinter import *
import os
from tkinter import messagebox

import mysql.connector
import azure.cognitiveservices.speech as speechsdk
import os
import mysql.connector

cnx = mysql.connector.connect(user="Vedant", password="Nogja@2004", host="mysql1249.mysql.database.azure.com", port=3306, database="doctor", ssl_ca="DigiCertGlobalRootCA.crt.pem", ssl_disabled=False)
print(cnx)

mycursor = cnx.cursor()


class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#166D3B")
        
        
       
        L1 = tk.Label(self, text="Username", font=("Arial Bold", 15), bg='#166D3B')
        L1.place(x=430, y=160)
        T1 = tk.Entry(self, width = 30, bd = 5)
        T1.place(x=550, y=160)
        
        L2 = tk.Label(self, text="Password", font=("Arial Bold", 15), bg='#166D3B')
        L2.place(x=430, y=200)
        T2 = tk.Entry(self, width = 30, show='*', bd = 5)
        T2.place(x=550, y=200)
        
        Label = tk.Label(self, text="!! MR.DOCTOR LOGIN !!", bg = "#166D3B",fg = "white",font=("Arial Bold", 20))
        Label.place(x=280, y=20)
        
        Label = tk.Label(self, text="The aim of medicine is to prevent \n disease  and prolong life, \n the ideal of medicine is to  \n eliminate  the need of a physician. \n Your health is our priority. \n Always Caring. Always Here.", bg = "#166D3B", fg = "white",font=("Monotype Corsiva", 18))
        Label.place(x=30, y=130)
        
        def verify():
            username = T1.get()
            password = T2.get()

            mycursor = cnx.cursor()

            sql = "SELECT username,password FROM user WHERE username = %s and password=%s"
            adr = (username, password)

            mycursor.execute(sql, adr)

            myresult = mycursor.fetchall()

            if len(myresult) == 1:
                controller.show_frame(ThirdPage)
                messagebox.showinfo(" Successfully login !!")
                # print("Successfully login")
                return True
            else:
                messagebox.showinfo("Error", "Please provide correct username and password!!")
                return False
            return True

        def admin():
            try:
                if "admin" == T1.get() and "1234" == T2.get():
                    controller.show_frame(FourthPage)
                    i = 1
                    if i==0:
                        messagebox.showinfo("Error", "Please provide correct username and password!!")
            except:
                messagebox.showinfo("Error", "Please provide correct username and password!!")
         
        B1 = tk.Button(self, text="Login",bg = "dark orange", font=("Arial", 15), command=verify)
        B1.place(x=660, y=300)
        
        B3 = tk.Button(self, text="Admin",bg = "dark orange", font=("Arial", 15), command=admin)
        B3.place(x=460, y=300)
        
        
        def register():
            window = tk.Tk()
            window.resizable(0,0)
            window.configure(bg="deep sky blue")
            window.title("Register")
            l1 = tk.Label(window, text="Username:", font=("Arial",15), bg="deep sky blue")
            l1.place(x=10, y=10)
            t1 = tk.Entry(window, width=30, bd=5)
            t1.place(x = 200, y=10)
            
            l2 = tk.Label(window, text="Password:", font=("Arial",15), bg="deep sky blue")
            l2.place(x=10, y=60)
            t2 = tk.Entry(window, width=30, show="*", bd=5)
            t2.place(x = 200, y=60)
            
            l3 = tk.Label(window, text="Confirm Password:", font=("Arial",15), bg="deep sky blue")
            l3.place(x=10, y=110)
            t3 = tk.Entry(window, width=30, show="*", bd=5)
            t3.place(x = 200, y=110)
            
            def check():
                if t1.get() != "" or t2.get() != "" or t3.get() != "":
                    if t2.get() == t3.get():
                        username = t1.get()
                        password = t2.get()
                        sql = "INSERT INTO user (username,password) VALUES (%s,%s)"
                        # sql = "INSERT INTO medicine (id,mname,cname,context,usedfor) VALUES (%s, %s,%s,%s, %s)"
                        val = (username, password)
                        mycursor.execute(sql, val)

                        cnx.commit()
                        #         with open("credential.txt", "a") as f:
                        #             f.write(t1.get()+","+t2.get()+"\n")
                        messagebox.showinfo("Welcome", "You are registered successfully!!")
                    else:
                        messagebox.showinfo("Error", "Your password didn't get match!!")
                else:
                    messagebox.showinfo("Error", "Please fill the complete field!!")


            b1 = tk.Button(window, text="Sign in", font=("Arial",15), bg="#ffc22a", command=check)
            b1.place(x=170, y=150)
            
            window.geometry("470x220")
            window.mainloop()
            
        B2 = tk.Button(self, text="Register", bg = "dark orange", font=("Arial",15), command=register)
        B2.place(x=550, y=300)
        
class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg="#00827F")

        Label(self, text="Name Search: ").grid(row=0, column=0, sticky='e')
        search_word = Entry(self, width=20)
        search_word.grid(row=0, column=1, padx=2, pady=2, sticky='we', columnspan=9)


        Label(self, text="Search Results: ").grid(row=4, column=0, sticky='e')
        d = Listbox(self, width=100, height=20, border=5)
        d.grid(row=4, column=4, padx=20, pady=40, sticky='we', columnspan=9)

        Label(self, text="Speak Here: ").grid(row=3, column=4, sticky='e')



        def speak ():

           # mname=speak.get()
           speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'),
                                                  region=os.environ.get('SPEECH_REGION'))
           speech_config.speech_recognition_language = "en-US"

           audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
           speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

           print("Speak into your microphone.")
           # print("Speak  Disease  name")
           # d.insert(1,"Speak  Disease  name")
           mname = speech_recognizer.recognize_once_async().get()


           if mname.reason == speechsdk.ResultReason.RecognizedSpeech:
               # print("Recognized: {}".format(mname.text))
               d.insert(1,format(mname.text))
           elif mname.reason == speechsdk.ResultReason.NoMatch:
               # print("No speech could be recognized: {}".format(mname.no_match_details))
               d.insert(1, format(mname.no_match_details))
           elif mname.reason == speechsdk.ResultReason.Canceled:
               cancellation_details = mname.cancellation_details
               # print("Speech Recognition canceled: {}".format(cancellation_details.reason))
               d.insert(1, format(cancellation_details.reason))
               if cancellation_details.reason == speechsdk.CancellationReason.Error:
                   # print("Error details: {}".format(cancellation_details.error_details))
                   d.insert(1, format(cancellation_details.error_details))
                   print("Did you set the speech resource key and region values?")

           speech_key, service_region = "14c6534add1b4f45bf844624212fa03f", "centralindia"
           speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

           # Set the voice name, refer to https://aka.ms/speech/voices/neural for full list.
           speech_config.speech_synthesis_voice_name = "en-US-AriaNeural"

           # Creates a speech synthesizer using the default speaker as audio output.
           speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
           mycursor = cnx.cursor()

           medicine_name = str(mname.text)
           medicine_name = medicine_name.split(".")
           print(medicine_name[0])
           sql1 = "SELECT * FROM medicine WHERE usedfor LIKE %s"
           sql = "SELECT * FROM medicine WHERE mname LIKE %s"
           cmd = ("%" + medicine_name[0] + "%",)
           mycursor.execute(sql, sql1, cmd)

           myresult = mycursor.fetchall()

           for x in range(0, len(myresult)):
               # Synthesizes the received text to speech.
               # The synthesized speech is expected to be heard on the speaker with this line executed.
               result = speech_synthesizer.speak_text_async(str(myresult[x])).get()

               # Checks result.
               if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                   # print("Speech synthesized to speaker for text [{}]".format(str(myresult[x])))
                   d.insert(1, format(str(myresult[x])))
               elif result.reason == speechsdk.ResultReason.Canceled:
                   cancellation_details = result.cancellation_details
                   print("Speech synthesis canceled: {}".format(cancellation_details.reason))
                   if cancellation_details.reason == speechsdk.CancellationReason.Error:
                       if cancellation_details.error_details:
                           print("Error details: {}".format(cancellation_details.error_details))
                   print("Did you update the subscription info?")

        def search():
            url=Entry.get()
            #---database.open(url)
    
        def content_analyser(pat):
            with open(pat,'r') as f:
                try:
                    for line in f:
                      if search in line:
                        d.update()
                        d.insert(END, pat)
                        break
                except:
                    pass
        def smali_finder(pat):
    
        
            try:
                for file in os.listdir(pat):
                    spat=pat+'/'+file 
                    if os.path.isdir(spat):
                        smali_finder(spat)
                    else:
                        if file.endswith(".smali"):
                            content_analyser(spat)
            except Exception as e:    
                print ("Error:::",pat,e)
        def fing(path):
            global search
            if search_word.get()=='':
                var=messagebox.showwarning(message="Please a search word")
        
            else:
                search=search_word.get()
                smali_finder(path)
        
        

   
    
    ###########################Buttons######################################
    
        start=Button(self,text="Start",bg="#20B2AA",command=search).grid(row=0,column=12,sticky='e'+'w',padx=2,pady=2)
    
        speak=Button(self,bg="#20B2AA",text="speak",command=speak).grid(row=3,column=5,sticky='e'+'w',padx=2,pady=2)
    
        Button(self,text="Exit",bg="red",command=lambda: controller.show_frame(ThirdPage)).grid(row=1,column=12,sticky='e'+'w',padx=2,pady=2)

     
    
        
class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg='Tomato')
        
        Label = tk.Label(self, text="MR.DOCTOR", bg = "Tomato", font=("Arial Bold", 35))
        Label.place(x=180, y=100)
        
        Label = tk.Label(self, text="Search The Medicine That You Want \n To Search.\n !! Always Be Healthy !!", bg = "orange", font=("Arial Bold", 25))
        Label.place(x=70, y=170)
        
        
        
        Button = tk.Button(self, text="Search Medicine",bg = "sky blue", font=("Arial", 15), command=lambda: controller.show_frame(SecondPage))
        Button.place(x=550, y=450)
        

class FourthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#00827F")
    

        L1 = tk.Label(self, text="Medicine Name", font=("Arial Bold", 15), bg='#166D3B')
        L1.place(x=200, y=100)
        T1 = tk.Entry(self, width = 30, bd = 5)
        T1.place(x=370, y=100)
        
        L2 = tk.Label(self, text="Company", font=("Arial Bold", 15), bg='#166D3B')
        L2.place(x=200, y=140)
        T2 = tk.Entry(self, width = 30, bd = 5)
        T2.place(x=370, y=140)
        
        L1 = tk.Label(self, text="Context", font=("Arial Bold", 15), bg='#166D3B')
        L1.place(x=200, y=180)
        T3 = tk.Entry(self, width = 30, bd = 5)
        T3.place(x=370, y=180)
        
        L2 = tk.Label(self, text="Used For", font=("Arial Bold", 15), bg='#166D3B')
        L2.place(x=200, y=220)
        T4 = tk.Entry(self, width = 30, bd = 5)
        T4.place(x=370, y=220)
        
        Label = tk.Label(self, text="!! MR.DOCTOR ADMIN !!", bg = "#166D3B",fg = "white",font=("Arial Bold", 20))
        Label.place(x=230, y=20)

        def addmed():

            sql = "INSERT INTO medicine (mname,cname,context,usedfor) VALUES ( %s,%s,%s, %s)"
            val = (T1.get(),T2.get(),T3.get(),T4.get())
            mycursor.execute(sql, val)

            cnx.commit()
        #
            print(mycursor.rowcount, "record inserted.")

        #Button & packing it and assigning it a command
        B4 = tk.Button(self, text=" Check Medicine",bg = "dark orange", font=("Arial", 15),command=lambda: controller.show_frame(SecondPage))
        B4.place(x=400, y=340)

        B5 = tk.Button(self, text=" Add Medicine", bg="dark orange", font=("Arial", 15),command=addmed)
        B5.place(x=200, y=340)

        
        
        

        
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #creating a window
        window = tk.Frame(self)
        window.pack()
        
        window.grid_rowconfigure(0, minsize = 500)
        window.grid_columnconfigure(0, minsize = 800)
        
        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage, FourthPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(FirstPage)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")
            
app = Application()
app.maxsize(800,500)
app.mainloop()
 
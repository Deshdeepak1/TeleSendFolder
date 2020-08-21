import os
import asyncio

try:
    from tkinter import *
except:
    os.system('sudo apt-get install python3-tk')
    os.system('apt-get install python-tkinter')
    from tkinter import *

try:
    from unidecode import unidecode
except:
    os.system('pip3 install unidecode')
    from unidecode import unidecode

from tkinter import messagebox , filedialog
from pyrogram import Client
from telegram_upload import files

API_ID=os.environ['API_ID']
API_HASH=os.environ['API_HASH']

loop=asyncio.get_event_loop()

async def sendVid(username,path):
  atr=files.get_file_attributes(path)
  print(atr)
  d=atr[0].duration
  w=atr[0].w
  h=atr[0].h
  thumb = files.get_file_thumb(path)
  caption = os.path.basename(path)
  print(atr[0])
  await client.send_video(username,path,caption=caption,duration=d,width=w,height=h,thumb=thumb,supports_streaming=True)

async def sendDoc(username,path):
    if files.get_file_mime(path)=='video':
        await sendVid(username,path)
    else:
        await client.send_document(username,path)


def upload (username,path,replacer):
  if os.path.isdir(path) :
    p=path.replace(replacer,'')
    loop.run_until_complete(client.send_message(username,p,parse_mode=None))
    print(path)
    Files=os.listdir(path)
    Files.sort()
    for file in Files :
      path=path+"/"+file
      upload(username,path,replacer)
      path= path.replace("/"+file,'')
      if file is Files[-1] :
          p=path.replace(replacer,'')         
          loop.run_until_complete(client.send_message(username,p,parse_mode=None))
          print(path)
  else:
    loop.run_until_complete(sendDoc(username,path))
    print(path)

class MainPage(Frame):

    def send(self):
        global client
        
        path=self.pathVar.get()
        username=self.userVar.get()
        try:
            username=int(username)
        except:
            pass
        username=1423220725
        replacer=os.path.dirname(path)+'/'
        upload(username,path,replacer)


    def chooseFolder(self):
        path=filedialog.askdirectory(title='Select Folder')
        self.pathVar.set(path)

    def __init__(self,app):
        global client
        Frame.__init__(self,app)
        self.config(bg='dark grey')

        self.f1 = Frame(self)
        self.f1.pack(fill=X,pady=10)

        self.pathL = Label(self.f1,text='Enter path: ',font='arial 14')
        self.pathL.pack(side=LEFT)
        
        self.pathVar=StringVar()
        self.pathB = Entry(self.f1,textvariable=self.pathVar,font='arial 14',width=35,highlightbackground='black')
        self.pathB.pack(side=LEFT)

        self.pathBtn = Button(self.f1,font='arial 14',text='Browse',width=8,highlightbackground='black',bg='light blue',command=self.chooseFolder)
        self.pathBtn.pack(side=LEFT,padx=4)

        self.f2 = Frame(self)
        self.f2.pack(fill=X,pady=2)

        self.userL = Label(self.f2,text='Enter username/id :  ',font='arial 14')
        self.userL.pack(padx=5,side=LEFT)

        self.userVar=StringVar()
        self.userB = Entry(self.f2,textvariable=self.userVar,font='arial 14',width=20,highlightbackground='black')
        self.userB.pack(padx=10,side=LEFT)
        self.userVar.set('me')
        
        self.f3 = Frame(self)
        self.f3.pack(fill=X,pady=2)

        self.sendB = Button(self.f3,text='Send',font='helvetica 14',bg='light blue',highlightbackground='grey',fg='green',width=8,command=self.send)
        self.sendB.pack()

        
class App(Tk):

        def __init__(self):
            global client

            Tk.__init__(self)
            self.title('Telegram Send Folder')
            self.geometry('700x130')
            self.resizable(0,0)
            self.config(bg='dark grey')

            api_id = int(API_ID)
            api_hash = API_HASH
            client = Client('my_account',api_id,api_hash)

            try:
                if loop.run_until_complete(client.connect()):
                    print('Connected')
                    mainPage=MainPage(self)
                    mainPage.pack(fill=BOTH,expand=True)
                else:
                    print('Not connected')
                    loginPage=LoginPage(self)
                    loginPage.pack(fill=BOTH,expand=True)
            except e:
                messagebox.showerror('Error',e)


if __name__=='__main__':
    app=App()
    app.mainloop()

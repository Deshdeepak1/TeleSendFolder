import os
import asyncio

try:
    from tkinter import *
except:
    os.system('sudo apt-get install python3-tk')
    os.system('apt-get install python-tkinter')
    from tkinter import *

from tkinter import messagebox , filedialog
from pyrogram import Client
from pyrogram.api.functions.channels import  GetAdminedPublicChannels

API_ID=os.environ['API_ID']
API_HASH=os.environ['API_HASH']

loop=asyncio.get_event_loop()

class MainPage(Frame):

    def chooseFolder(self):
        path=filedialog.askdirectory(title='Select Folder')
        self.pathVar.set(path)

    def __init__(self,app):
        global client
        Frame.__init__(self,app)
        self.config(bg='dark grey')

        self.f1 = Frame(self)
        self.f1.pack(fill=X,pady=30)

        self.pathL = Label(self.f1,text='Enter path: ',font='arial 14')
        self.pathL.pack(side=LEFT)
        
        self.pathVar=StringVar()
        self.pathB = Entry(self.f1,textvariable=self.pathVar,font='arial 14',width=35,highlightbackground='black')
        self.pathB.pack(side=LEFT)

        self.pathBtn = Button(self.f1,font='arial 14',text='Browse',width=10,highlightbackground='black',bg='light blue',command=self.chooseFolder)
        self.pathBtn.pack(side=LEFT,padx=5)

        users=[]
        groups=[]
        channels=[]
        
        #async def dial():
        #    async for dialog in client.iter_dialogs():
        #        if dialog.chat.type=="channel":
        #            print(dialog.chat.title,dialog.chat)
        #loop.run_until_complete(dial())
        channels=GetAdminedPublicChannels()
        print(channels)

class App(Tk):

        def __init__(self):
            global client

            Tk.__init__(self)
            self.title('Telegram Send Folder')
            self.geometry('700x850')
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

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
        self.f1.pack(fill=X,pady=10)

        self.pathL = Label(self.f1,text='Enter path: ',font='arial 14')
        self.pathL.pack(side=LEFT)
        
        self.pathVar=StringVar()
        self.pathB = Entry(self.f1,textvariable=self.pathVar,font='arial 14',width=35,highlightbackground='black')
        self.pathB.pack(side=LEFT)

        self.pathBtn = Button(self.f1,font='arial 14',text='Browse',width=10,highlightbackground='black',bg='light blue',command=self.chooseFolder)
        self.pathBtn.pack(side=LEFT,padx=5)

        channels=[]
        groups=[]
        users=[]
        
        async def dial():
            async for dialog in client.iter_dialogs():
                if dialog.chat.type=="channel"  :
                    channels.append(dialog.chat)
                elif dialog.chat.type in ["group","supergroup"] :
                    groups.append(dialog.chat)
                elif dialog.chat.type == "private" and dialog.chat.first_name!=None:
                    users.append(dialog.chat)
        loop.run_until_complete(dial())
        
        self.f2 = Frame(self)
        self.f2.pack(fill=X,pady=2)

        self.meRb = Radiobutton(self.f2,text="ME",font='veranda 14')
        self.meRb.pack(fill=BOTH)

        self.f3 = Frame(self)
        self.f3.pack(fill=BOTH)

        self.f3a = Frame(self.f3)
        self.f3a.pack(fill=X,side=TOP)
        
        self.f3a1 = Frame(self.f3a)
        scroll1 = Scrollbar(self.f3a1)
        scroll1.pack(side=RIGHT,fill=Y)
        self.f3a1.config(yscrollcommand=scroll1.set)
        self.f3a1.pack(fill=Y,side=LEFT)
        
        self.f3a2 = Frame(self.f3a)
        scroll2 = Scrollbar(self.f3a2)
        scroll2.pack(side=RIGHT,fill=Y)
        self.f3a1.config(yscrollcommand=scroll2.set)
        self.f3a2.pack(fill=Y,side=LEFT)
        
        self.f3a3 = Frame(self.f3a)
        scroll3 = Scrollbar(self.f3a3)
        scroll3.pack(side=RIGHT,fill=Y)
        self.f3a1.config(yscrollcommand=scroll3.set)
        self.f3a3.pack(fill=Y,side=LEFT)

        self.f3b = Frame(self.f3)
        self.f3b.pack(fill=X,pady=3,side=BOTTOM)

        self.sendB = Button(self.f3b,text='Send',font='helvetica 16',bg='light blue',highlightbackground='grey',fg='green',width=10)
        self.sendB.pack(pady=5)

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

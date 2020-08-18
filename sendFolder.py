import os

try:
  import asyncio
except:
  os.system('pip3 install -U asyncio')
  import os

try:
  from pyrogram import Client
  from telegram_upload import files
except:
  os.system('pip3 install -U https://github.com/pyrogram/pyrogram/archive/asyncio.zip tgcrypto telegram-upload')
  from pyrogram import Client
  from telegram_upload import files

loop=asyncio.get_event_loop()

api_id = 1323261
api_hash = "695d0d4bf6f348f82d29e41eea411823"
client = Client('my_account',api_id,api_hash)

async def go():
 await client.start()

loop.run_until_complete(go())

async def sendMsg(msg):
    await client.send_message(username,msg,parse_mode=None)

async def sendVid(path):
  atr=files.get_file_attributes(path)
  print(atr)
  d=atr[0].duration
  w=atr[0].w
  h=atr[0].h
  thumb = files.get_file_thumb(path)
  caption = os.path.basename(path)
  print(atr[0])
  await client.send_video(username,path,caption=caption,duration=d,width=w,height=h,thumb=thumb,supports_streaming=True)

path=input('Enter path : ')
username = input("Enter phone no. , channel link, group link ,etc. : ")

def upload (path):
  if os.path.isdir(path) :
    p=path.replace(replacer,'')
    loop.run_until_complete(sendMsg(p))
    print(path)
    Files=os.listdir(path)
    Files.sort()
    for file in Files :
      path=path+"/"+file
      upload(path)
      path= path.replace("/"+file,'')
      if file is Files[-1] :
          p=path.replace(replacer,'')         
          loop.run_until_complete(sendMsg(p))
          print(path)
  else:
    loop.run_until_complete(sendVid(path))
    print(path)

replacer=os.path.dirname(path)+'/'
upload(path)

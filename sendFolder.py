import os
import asyncio
from pyrogram import Client
from telegram_upload import files

API_ID=os.environ['API_ID']
API_HASH=os.environ['API_HASH']

loop=asyncio.get_event_loop()

api_id = int(API_ID)
api_hash = API_HASH

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

async def sendDoc(path):
    if files.get_file_mime(path)=='video':
        await sendVid(path)
    else:
        await client.send_document(username,path)

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
    loop.run_until_complete(sendDoc(path))
    print(path)

def main():
  global username,replacer,client
  
  files=os.listdir()
  sessions=[]
  for file in files:
    if file.endswith('.session'):
      sessions.append(file)
  
  i=0
  phones=[]
  for session in sessions:
    phones.append(session.split('.session')[0])
    client=Client(phones[i],api_id,api_hash)
    loop.run_until_complete(client.connect())
    
    me=loop.run_until_complete(client.get_me())
    try:
        name=me['first_name']+' '+me['last_name'] 
    except:
        name=me['first_name']    
    name=name+'\n ('+me['phone_number']+')'
    print(str(i+1)+". "+name)
    loop.run_until_complete(client.disconnect())
    i+=1

  print(str(i+1)+". New login")

  c=int(input("Enter valid choice: "))
  if c==len(phones)+1:
    phone=input("Enter phone: ")
    client=Client(phone,api_id,api_hash)
    loop.run_until_complete(client.connect())
    code_hash=loop.run_until_complete(client.send_code(phone))['phone_code_hash']
    code=input("Enter code: ")
    loop.run_until_complete(client.sign_in(phone,code_hash,code))
  else:
    client=Client(phones[c-1],api_id,api_hash)
    loop.run_until_complete(client.connect())

  me=loop.run_until_complete(client.get_me())
  try:
    name=me['first_name']+' '+me['last_name'] 
  except:
    name=me['first_name']
  wel="Logged in as: "+name+' ('+me['phone_number']+')\n'
  print(wel)
  path=input('Enter path : ')
  username = input("Enter phone no. , channel link, group link ,etc. : ")
  replacer=os.path.dirname(path)+'/'
  upload(path)


if __name__ == "__main__":
    main()
# TeleSendFolder
 Telegram folder sender built in python.

# Instructions for termux & linux.
 1. git clone https://github.com/Deshdeepak1/TeleSendFolder.git
 2. cd TeleSendFolder
 3. chmod  ./sendFolder.sh ./sendFolder1.sh
 4. Set environment variables API_ID & API_HASH
 5. First time: ./sendFolder1.sh 
 6. Next time: ./sendFolder.sh 
 7. Give root/sudo privilege if required.


# Instructions for windows.
 1. git clone https://github.com/Deshdeepak1/TeleSendFolder.git or download zip
 2. cd TeleSendFolder or move inside folder
 3. Set environment variables API_ID & API_HASH.
 4. First time:-
   a. Start powershell as administrator 
   b. Set-ExecutionPolicy unrestricted
   c. .\win10.PS1
 5. Next time: Start sendFolder.py or sendFolderGui.py

# On error.
	If authorization error occurs, delete all(which are corrupted/unauthorised) session files.
	Else if tkinter error, find how to install tkinter on your os.
	Else if ffmpeg error, find how to install ffmpeg on your os.

#!/bin/bash
sudo apt install ffmpeg
apt install ffmpeg
sudo yum install ffmpeg
pip3 install -U -r requirements.txt
read choice
echo $choice
if [ $choice = 1 ]
then
    python3 sendFolder.py
elif [ $choice = 2 ]
then
    sudo apt-get install python3-tk
    sudo yum install python3-tk
    apt-get install python-tkinter
    python3 sendFolderGui.py
else
    printf "Invalid choice\n"
fi

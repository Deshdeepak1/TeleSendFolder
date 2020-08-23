#!/bin/bash
printf "1.Cli\n2.Gui\nEnter choice: " 
read choice
if [ $choice = 1 ]
then
    python3 sendFolder.py
elif [ $choice = 2 ]
then
    python3 sendFolderGui.py
else
    printf "Invalid choice\n"
fi

#!/bin/bash

apt install ffmpeg
pip3 install -U -r requirements.txt
python3 sendFolder.py

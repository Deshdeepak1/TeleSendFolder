wget https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-20200816-5df9724-win64-static.zip
sleep 60
expand-archive ffmpeg-* ffmpeg
sleep 10
cp ffmpeg\ffmpeg-*\bin\* C:\Windows\System32
pip3 install -U -r requirements.txt
python sendFolder.py
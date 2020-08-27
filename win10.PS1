$url = "https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-20200816-5df9724-win64-static.zip"
$output = "ffmpeg.zip"
$start_time = Get-Date

Import-Module BitsTransfer
Start-BitsTransfer -Source $url -Destination $output
#OR
Start-BitsTransfer -Source $url -Destination $output -Asynchronous
sleep 5

expand-archive ffmpeg.zip ffmpeg
sleep 3

cp ffmpeg\ffmpeg-*\bin\* C:\Windows\System32

pip3 install -U -r requirements.txt

$choice = Read-Host -prompt "1.Cli`n2.Gui`nEnter choice: "
If ($choice -eq '1'){
python sendFolder.py
} ElseIf ($choice -eq '2'){
python sendFolderGui.py
} Else {
echo "Invalid Choice"
}

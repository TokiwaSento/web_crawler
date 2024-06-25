import re
from moviepy.editor import *
import requests
import json
import os

head = {
    'referer': 'https://www.bilibili.com/',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; X64"}
url = input('复制你要下载的b站视频连接：')
response = requests.get(url, headers=head)

play_info = re.findall('window.__playinfo__=(.*?)</script>', response.text)[0]
json_data = json.loads(play_info)
print(json_data)

video = json_data['data']['dash']['video'][0]['baseUrl']
video_data = requests.get(video, headers=head).content
with open('1.mp4', mode='wb') as f:     #追加写入就是把wb换成ab
    f.write(video_data)
del video

audio = json_data['data']['dash']['audio'][0]['baseUrl']
audio_data = requests.get(audio, headers=head).content
with open('1.mp3', mode='wb') as f:     #wb是覆写，追加写入就是把wb换成ab
    f.write(audio_data)
del audio

video = VideoFileClip('E:/MyWork/IDPS/Climb_bug/1.mp4')
audio = AudioFileClip('E:/MyWork/IDPS/Climb_bug/1.mp3')
video = video.set_audio(audio)
video.write_videofile("E:/MyWork/IDPS/Climb_bug/output.mp4", codec='libx264')
os.remove('E:/MyWork/IDPS/Climb_bug/1.mp4')
os.remove('E:/MyWork/IDPS/Climb_bug/1.mp3')
"""
with open('1.mp4', mode='wb') as f:     #追加写入就是把wb换成ab
    f.write(response.content)
"""
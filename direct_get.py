import requests
head = {
    'referer': 'https://www.bilibili.com/',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; X64",
    }
url = input('复制你要下载的视频url：')
video_data = requests.get(url, headers=head).content
with open('1.mp4', mode='wb') as f:     #追加写入就是把wb换成ab
    f.write(video_data)
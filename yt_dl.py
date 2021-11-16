import youtube_dl
import sys


class YT_Downloader():
    def __init__(self):
        pass

    def download_mp3(self, url, path):
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': path + '%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("Downloaded")
        except:
            print("Error downloading mp3")

    def download_mp4(self, url, path):
        try:
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': path + '%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("Downloaded")
        except:
            print("Error downloading mp3")

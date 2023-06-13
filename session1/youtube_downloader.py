import os

from pytube import YouTube

os.chdir("/Users/valentin/Documents/VHS Kurse/Automatisierung mit Python/Demo Ordner")

print(os.getcwd())

url = input("bitte Link geben: ")

video = YouTube(url)

print(video.title)

best_video = video.streams.get_highest_resolution()

audio = video.streams.filter(only_audio=True).first()

audio_file = audio.download()

filename, file_type = os.path.splitext(audio_file)

new_file_name = filename + ".mp3"

os.rename(audio_file, new_file_name)

os.mkdir("musik")

os.rename(new_file_name, os.getcwd() + "/musik/" + "song1" + ".mp3")

best_video.download()


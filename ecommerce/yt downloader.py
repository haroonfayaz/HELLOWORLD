import pytube


save_path = "E:/"
url = "https://youtu.be/hSnwf9aPcJU"
youtube = pytube.YouTube(url)
streams = youtube.streams.all()
for i in streams:

    print(i)

video = youtube.streams.get_by_itag(278)
video.download(save_path)
print("task completed")


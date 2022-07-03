# importing packages
from pytube import YouTube
from pytube import Playlist
import os
  
# url input from user
yt = Playlist(
    str(input("Enter the URL of the playlist you want to download: \n>> ")))

# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'
  
# extract only audio
for video in yt.videos:
    video = video.streams.filter(only_audio=True).first()
  
    # download the file
    out_file = video.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    # result of success
    print(video.title + " has been successfully downloaded.")

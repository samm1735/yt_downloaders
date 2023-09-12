from pytube import YouTube


link = 'https://www.youtube.com/watch?v=cACat4KNncg&pp=ygUTc3FsIHNlcnZlciB0dXRvcmlhbA%3D%3D'


video = YouTube(link)

print(f"you're rying to download {video.title}")



stream = video.streams.get_highest_resolution()

print(stream)

# Download the video
print(f"Downloading: {video.title}")
stream.download(output_path='download_directory')
print(f"Downloaded: {video.title}")



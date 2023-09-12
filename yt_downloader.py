from pytube import Playlist

# URL of the YouTube playlist
playlist_url = 'https://www.youtube.com/playlist?list=PLN7okjUrNatrHbODlMgTRJ01P8ltZFGI5'

# Create a Playlist object
playlist = Playlist(playlist_url)

# Loop through each video in the playlist
for video in playlist.videos:
    # Get the highest resolution stream (1080p)
    stream = video.streams.get_highest_resolution()

    # Download the video
    print(f"Downloading: {video.title}")
    stream.download(output_path='download_directory')
    print(f"Downloaded: {video.title}")

from src.check_youtube_url import check_youtube_url
from pytubefix import YouTube, Playlist
from tqdm import tqdm
import os

def download_media(url, output_path, audio_only=False):
    if not check_youtube_url(url):
        raise ValueError("Invalid YouTube URL")

    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=audio_only).first() if audio_only else yt.streams.get_highest_resolution()
    total_size = stream.filesize

    def progress_function(stream, chunk: bytes, bytes_remaining: int):
        size = total_size - bytes_remaining
        pbar.update(size - pbar.n)

    with tqdm(total=total_size, unit='B', unit_scale=True, desc=yt.title, ncols=150) as pbar:
        yt.register_on_progress_callback(progress_function)
        output_file = stream.download(output_path)
    
    if audio_only:
        base, _ = os.path.splitext(output_file)
        new_file = base + '.mp3'
        os.rename(output_file, new_file)
        print(f"Audio '{yt.title}' downloaded successfully!")
    else:
        print(f"Video '{yt.title}' downloaded successfully!")

def download_video(url, output_path):
    try:
        download_media(url, output_path, audio_only=False)
    except Exception as e:
        print(f"Error downloading video: {str(e)}")

def download_audio(url, output_path):
    try:
        download_media(url, output_path, audio_only=True)
    except Exception as e:
        print(f"Error downloading audio: {str(e)}")

def download_playlist(url, output_path):
    if not check_youtube_url(url):
        raise ValueError("Invalid YouTube URL")

    try:
        pl = Playlist(url)
        for video in pl.videos:
            download_audio(video.video_id, output_path)
        print(f"All videos in playlist '{pl.title}' downloaded successfully!")
    except Exception as e:
        print(f"Error downloading playlist: {str(e)}")

from src.download_and_convert import download_audio, download_playlist, download_video
from src.get_standard_path import get_standard_paths
from src.validate_output_path import validate_output_path

MUSIC_PATH, MEDIA_PATH = get_standard_paths()
  
def youtube_downloader(): 
    url = input("Enter the YouTube video URL: ").strip()
    choice = input("Do you want to download video or audio or playlist? (v/a/p): ").strip().lower()

    output_path_input = input("Enter output path (leave blank for default directories): ").strip()
    
    if not output_path_input:
        output_path = None
    else:
        output_path = validate_output_path(output_path_input)
    
    if choice == 'v':
        download_video(url, output_path=output_path or MEDIA_PATH)
    elif choice == 'a':
        download_audio(url, output_path=output_path or MUSIC_PATH)
    elif choice == 'p':
        download_playlist(url, output_path=output_path or MUSIC_PATH)
    else:
        print("Invalid choice. Please enter 'v' for video, 'a' for audio, or 'p' for playlist.")

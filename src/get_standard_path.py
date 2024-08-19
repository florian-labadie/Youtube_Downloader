import os
import platform

def get_standard_paths():
    system = platform.system()
    home_dir = os.path.expanduser("~")
    
    if system == "Windows":
        music_path = os.path.join(os.environ.get('USERPROFILE', home_dir), "Music")
        videos_path = os.path.join(os.environ.get('USERPROFILE', home_dir), "Videos")
    else:  # For Unix-like (Linux, macOS)
        music_path = os.path.join(home_dir, "Music")
        videos_path = os.path.join(home_dir, "Videos")
    
    return music_path, videos_path

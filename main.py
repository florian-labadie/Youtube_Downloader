from src.youtube_downloader import youtube_downloader
import sys

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            if sys.argv[1] == '--non-interactive':
                youtube_downloader(non_interactive=True)
            else:
                print("Usage: ./price_game [--non-interactive]")
        else:
            youtube_downloader()
    except ValueError as ve:
        print(f"Error: {ve}")
        exit(-84)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(84)

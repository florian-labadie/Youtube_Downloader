from src.youtube_downloader import youtube_downloader

if __name__ == '__main__':
    try:
        youtube_downloader()
    except ValueError as ve:
        print(f"Error: {ve}")
        exit(-84)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(84)

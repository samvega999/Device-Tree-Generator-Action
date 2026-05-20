import yt_dlp

def simple_download(url, path="downloads"):
    """Simple function to download a YouTube video"""
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{path}/%(title)s.%(ext)s',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Usage
simple_download("https://youtu.be/pOpVtzysJf4?si=dNNTCnJHqDezTK7J")

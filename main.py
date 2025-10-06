import os
import subprocess
import time

# 🔑 Stream key Render ke Environment me set karna (YOUTUBE_STREAM_KEY)
YOUTUBE_URL = f"rtmp://a.rtmp.youtube.com/live2/{os.getenv('YOUTUBE_STREAM_KEY')}"

# 🎥 Google Drive se video link (Direct Download link banana zaroori hai)
# Example: https://drive.google.com/uc?export=download&id=YOUR_FILE_ID
VIDEO_URL = "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID"

def start_stream():
    while True:
        print("🔴 Starting YouTube stream...")
        cmd = [
            "ffmpeg",
            "-re",
            "-stream_loop", "-1",
            "-i", VIDEO_URL,
            "-c:v", "libx264",
            "-preset", "veryfast",
            "-b:v", "3000k",
            "-maxrate", "3000k",
            "-bufsize", "6000k",
            "-pix_fmt", "yuv420p",
            "-g", "50",
            "-c:a", "aac",
            "-b:a", "128k",
            "-ar", "44100",
            "-f", "flv",
            YOUTUBE_URL
        ]
        try:
            subprocess.run(cmd)
        except Exception as e:
            print("⚠️ Error:", e)
        print("🔁 Restarting stream in 5 seconds...")
        time.sleep(5)

if __name__ == "__main__":
    start_stream()

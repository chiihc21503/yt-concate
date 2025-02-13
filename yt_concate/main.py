import subprocess


def get_video_ids(channel_url):
    command = ["yt-dlp", "--flat-playlist", "--print", "id", channel_url]

    result = subprocess.run(
        command, capture_output=True, text=True, check=True
    )

    video_ids = result.stdout.strip().split("\n")
    return video_ids


channel_url = "https://www.youtube.com/@SupercarBlondie"

video_ids = get_video_ids(channel_url)

video_urls = []
for video_id in video_ids:
    video_url = 'https://www.youtube.com/watch?v=' + video_id
    video_urls.append(video_url)

print(len(video_urls))

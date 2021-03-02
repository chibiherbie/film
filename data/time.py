from time import sleep
from moviepy.editor import VideoFileClip


def get_lenght(file_num):
    file = f'video/{file_num}.mp4'
    clip = VideoFileClip(file)
    return clip.duration

print('ha-ha')
sleep(get_lenght(2))
print('ha')
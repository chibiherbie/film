'''
from os import startfile
startfile('/Users/alekseyostrovskiy/Desktop/film/data/video/2.mp4')
'''
import os
print(os.path.abspath('1.mp4'))
import cv2
from ffpyplayer.player import MediaPlayer
video_path="/Users/alekseyostrovskiy/Desktop/film/data/video/2.mp4"
def PlayVideo(video_path):
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()
PlayVideo(video_path)
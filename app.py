import os

ffmpeg_bin = '/var/task/ffmpeg.linux64'
os.environ['FFMPEG_BINARY'] = ffmpeg_bin
os.environ['IMAGEIO_FFMPEG_EXE'] = ffmpeg_bin

from moviepy.editor import *

def lambda_handler(event=None, context=None):
    print('HelloWorld')
    # print('Event time was: %s', event['time'])
    # print('This log is:', context.log_group_name, context.log_stream_name)
    # print('Time left for execution:', context.get_remaining_time_in_millis())

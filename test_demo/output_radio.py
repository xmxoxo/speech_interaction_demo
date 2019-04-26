# -*- coding: utf-8 -*-
# @Time     :2018/9/11
# @Author   :qpf


"""
播放音频文件
"""
from pygame import mixer

import pygame
import traceback
import logging
import os


# 播放MP3文件 
def speak(fname):
    try:
        # frequency用来控制语速，去掉试一下就明白了。。。
        mixer.init(frequency=16000, size=0)
        mixer.music.load(fname)
        mixer.music.play()
        while mixer.music.get_busy():
            continue
        mixer.music.stop()
        mixer.quit() 
        print('声音播放完毕')
    except Exception as e :
        print(e)
        return None

#播放MP3 使用playsound
#autodel 播放完后自动删除文件，默认 否
def playMp3(fname,autodel = 0):
    pass
    try:
        from playsound import playsound
        playsound(fname)
        if autodel:
            os.remove (fname)
    except Exception as e :
        #logging.error('Error in playMp3: '+ traceback.format_exc())
        return None


if __name__ == '__main__':
    speak(".\\tmp\\tuling-answer.mp3")

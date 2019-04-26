#!/usr/bin/env python3
#coding:utf-8

__author__ = 'xmxoxo<xmxoxo@qq.com>'

import os
import sys

class RobotConfig():
    # 百度需要的参数
    APP_ID = ''
    API_KEY = ''
    SECRET_KEY = ''

    # 图灵需要的参数
    TULING_KEY = ''

    # 录音的时间长度(秒）
    gblInt_Record_Seconds = 5

    # 临时文件的目录与名称
    temp_folder = 'tmp'

    temp_folder = os.path.join(".",temp_folder)

    #录音文件名
    wavfile_path =  os.path.join(temp_folder , 'record-audio.wav') 

    #回复内容转成语音后的MP3文件名
    tuling_answer_file = os.path.join(temp_folder , 'tuling-answer.mp3')
    
    #是否播放问候语
    gbl_Bool_Play_Tip = 1

    #问候语文字
    Voice_Tip_text = "亲，我在呢！有啥事？"

    #问候语转换后的声音文件，如要重新生成请删除该文件，下次启动会自动生成。
    Voice_Tip_mp3 = os.path.join(temp_folder , 'Tip.mp3')

    #退出词
    Quit_words = ['再见', '拜拜','我走了']


if __name__ == '__main__':
    pass


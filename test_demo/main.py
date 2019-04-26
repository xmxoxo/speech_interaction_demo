# -*- coding: utf-8 -*-
# @Time     :2018/9/4
# @Author   :qpf

import os
import sys
import random
import string 
import traceback
import logging

#from test_demo 
import input_record, recognition_speech, tuling_robot

from compound_speech import *
from output_radio import *
from RobotConfig import *

class VoiceRobot():

    #文字转成语音
    def t2v (self, strText, strFileName):
        text2voice(self.config.APP_ID, self.config.API_KEY, self.config.SECRET_KEY, strText, strFileName)
        
    #初始化
    def __init__(self, config):
        self.config = config
        
        #指定默认的回复方法 
        self.answer = self._fun_echo

        #创建目录
        if not os.path.exists(config.temp_folder):
            os.makedirs (self.config.temp_folder)

        #生成问候语
        if not os.path.exists(self.config.Voice_Tip_mp3):
            self.t2v (self.config.Voice_Tip_text, self.config.Voice_Tip_mp3)
        
        #删除临时文件
        self.del_tmpfile()

    #默认回复方法：原样返回
    def _fun_echo (self,x):
        return x
        
    #指定回答的方法
    def answer(self,answer_fun):
        self.answer = answer_fun
        return 1

    #清除临时文件
    def del_tmpfile (self):
        print("正在删除临时文件...")
        #os.system("del %s" % self.config.wavfile_path )
        os.system("del %s" % os.path.join(self.config.temp_folder , "tuling-answer_*.mp3") )


    #运行
    def run (self):
        pass

        while 1:
            #播放问候语
            if self.config.gbl_Bool_Play_Tip:
                speak(self.config.Voice_Tip_mp3)

            # 先调用录音，录10秒
            print('准备录音...')
            bRet = input_record.record(self.config.wavfile_path , self.config.gblInt_Record_Seconds)
            if not bRet:
                break;

            # 语音转成文字的内容
            print('声音转文字...')
            input_message = recognition_speech.voice2text(self.config.APP_ID, \
                    self.config.API_KEY, self.config.SECRET_KEY, self.config.wavfile_path)

            print('[你说]:' ,  input_message)
            #print(type(input_message))
            # 没有识别到则继续
            if not input_message:
                continue

            # 获取回答信息
            answer = self.answer(input_message[0]) 
            print("[回答]:%s" % answer)

            # 随机生成语音文件
            #tuling_answer_file = './tmp/tuling-answer_'+ get_randstr() + '.mp3'
            tuling_answer_file = os.path.join(self.config.temp_folder , 'tuling-answer_' + get_randstr() + '.mp3' )
            print('机器人语音文件: %s '  % tuling_answer_file)

            print('文字转声音...')
            self.t2v (answer, tuling_answer_file)

            # 播放图灵回答的内容
            print('播放声音...')
            speak(tuling_answer_file)
            #playMp3 (tuling_answer_file)
            
            #判断退出词
            if input_message[0] in self.config.Quit_words:
                break
        
        #删除临时文件, 在这里删除好象有些文件删除不了
        self.del_tmpfile()


def myanswer (x):
    print("图灵机器人接口...")
    answer = tuling_robot.answer(x, RobotConfig.TULING_KEY)
    # 将文字转化为语音
    text = answer['text']
    if answer['code']==302000:
        text = ''
        p = random.randint(0,len(answer['list'])-1) 
        text += '，'+ answer['list'][p]['article']
        #  random.randint(0,len(answer['list']))
    return text

#手机评论API接口
def mobileApi (txt):
    pass
    print("手机评论模型接口...")
    
    import requests
    import json

    url = 'http://192.168.15.111:8910/api/v0.1/query'
    dt = {'text': txt}
    res = requests.post(url, data=dt)
    res.encoding = 'utf-8'
    answer_message = json.loads(res.text)
    return answer_message['result'][0][0]
    
#把评论情感转换成句子
def mobile_answer(txt):
    if txt in self.config.Quit_words:
        x = 3
    else:
        x = int(mobileApi(txt)) + 1
        print(x)
    import random 
    emotions = [
                #差评
                ['呜~呜~呜~, 好伤心啊, 您的评价这么差么',
                '东西真的有这么差么，你是猴子请来的救兵吗？',
                '不喜欢也不要说得这么直白嘛！',
                '好吧亲，我们会努力做得更好一点的！',
                '亲，真不好意思，你要是不喜欢就换一个呗？',
                ],

                #中评
                ['您的评论情感是中性的',
                '我们的产品还是有很多优点的，有待慢慢发现呢。',
                '我们的产品还需要改进，嗯，我会努力的。',
                '看来你还没发现我的优点，哈哈。',

                ],
                
                #好评
                ['谢谢亲的好评，嗯，我会加油的！么么哒',
                '您的评论情感充满正能量！谢谢你',
                '看你这么喜欢我们的产品，我的付出是值得的！',
                ],
                
                #退出词回复
                ['亲，您走好。',
                '走好不送。',
                '亲，你就这样走了么，我会想你的。',
                ],
               ]
    intLen = len(emotions[x])
    intIndex = random.randint(0,intLen-1)
    return emotions[x][intIndex]

    

if __name__ == '__main__': 
    #config = RobotConfig()
    robot = VoiceRobot(RobotConfig())


    #指定回答接口
    print('正在指定回复接口...')
    #robot.answer = myanswer
    robot.answer = mobile_answer

    #运行机器人
    robot.run()

    '''
    txt = mobile_answer("物流实在不敢恭维，手机电池也太容易没电了。")
    txt = mobile_answer("物流实在不错，手机电池也很耐用呢。")
    print(txt)
    robot.t2v (txt, RobotConfig.tuling_answer_file)
    speak(RobotConfig.tuling_answer_file)
    '''
# -*- coding: utf-8 -*-
# @Time     :2018/9/4
# @Author   :qpf


"""
保存说话音频
"""

import pyaudio
import wave

#发出提示音
def BeepTip (sound = 600, timeLong = 500):
    import winsound
    winsound.Beep(sound,timeLong)

def record(file_path, rec_seconds = 5):
    try:
        # 各路参数
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        RECORD_SECONDS = rec_seconds  #录音5秒
        WAVE_OUTPUT_FILENAME = file_path
        pau = pyaudio.PyAudio()

        stream = pau.open(format=FORMAT,
                          channels=CHANNELS,
                          rate=RATE,
                          input=True,
                          frames_per_buffer=CHUNK, )

        frames = []

        BeepTip(900,500)
        print("开始录音")

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("结束录音")
        BeepTip(600,500)

        stream.stop_stream()
        stream.close()
        pau.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(pau.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        return 1
    except Exception as e :
        print("系统无法录音，请检查录音硬件设备情况...")
        print(e)
        return None

import sys
import time
import datetime

from screen_recorder_sdk import screen_recorder 
import PIL.ImageGrab

import pyaudio
import wave


class screenRecord:
        def start(self,seconds=30,filename=None,frame=30,bitrate=8000000,useGPU=False,countdown=5,echo=True):
                try:
                        if filename==None:
                                time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
                                filename = f'{time_stamp}'+'_'+str(seconds)+'seconds.mp4'


                        if countdown!=0:
                                for i in range(countdown,0,-1):
                                        if echo: print('Recording Starts in: ',i,' seconds')
                                        time.sleep(1)


                        screen_recorder.enable_dev_log ()
                        params = screen_recorder.RecorderParams ()
                        #intialize the screen recoder
                        screen_recorder.init_resources (params)

                        #start video recording
                        if echo: print('Recording Started for '+str(seconds)+' seconds')
                        screen_recorder.start_video_recording (filename, frame, bitrate, useGPU)

                        time.sleep (seconds)
                        screen_recorder.stop_video_recording ()
                        if echo: print('Recording Stopped')
                        return True
                
                except Exception as e:
                        print('Error in Screen Recording')
                        print(e)
                        return False



class micRecord():
        def start(self,seconds=30,filename=None,chunk=1024,channels=2,rate=44100,countdown=5,echo=True):

                if filename==None:
                                time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
                                filename = f'{time_stamp}'+'.wav'

                for i in range(countdown,0,-1):
                                if echo: print('Time remaining: ',i)
                                time.sleep(1)

                sample_format = pyaudio.paInt16
                p = pyaudio.PyAudio()

                if echo: print('Recording')

                stream = p.open(format=sample_format,
                                channels=channels,
                                rate=rate,
                                frames_per_buffer=chunk,
                                input=True)

                frames = []
                # Store data in chunks for 3 seconds
                for i in range(0, int(rate / chunk * seconds)):
                    data = stream.read(chunk)
                    frames.append(data)

                stream.stop_stream()
                stream.close()
                p.terminate()


                if echo: print('Finished recording')

                # Save the recorded data as a WAV file
                wf = wave.open(filename, 'wb')
                wf.setnchannels(channels)
                wf.setsampwidth(p.get_sample_size(sample_format))
                wf.setframerate(rate)
                wf.writeframes(b''.join(frames))
                wf.close()

                return True




class screenshot():
        def capture(self,countdown=5,filename=None,extension='png',echo=True):
                try:
                        if filename==None:
                                time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
                                filename = f'{time_stamp}'

                        for i in range(countdown,0,-1):
                                if echo: print('Time remaining: ',i)
                                time.sleep(1)

                        im = PIL.ImageGrab.grab()
                        im.save(filename+'.'+extension)

                        if echo: print('Scroonshot Captured')
                        return True
                
                except Exception as e:
                        print('Error in taking screenshot')
                        print(e)
                        return False



if __name__ == "__main__":
    pass
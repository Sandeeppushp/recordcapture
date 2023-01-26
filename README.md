# recordcapture
recordcapture is a library based on Desktop Duplication API, pillow, and pyaudio which provide multiple methods for capturing and recording Screen and Microphone.



# Usuage:

import recordcapture


sr=recordcapture.screenRecord()<br>
sr.start(seconds=30,filename=None,frame=30,bitrate=8000000,useGPU=False,countdown=5,echo=True) <br>
#Note: All Parameters are optional<br>
seconds: total time to record the screen in seconds<br>
filename: any filename eg: abc.mp4, if not provided, will take timestamp as default.<br>
frame: frame per second.<br>
bitrate: bit processed per unit of time<br>
useGPU: using gpu for enhanced the recording, if face issue the  put as False<br>
countdown: countdown before start recording<br>
echo: to print the event messages<br>
<br>
<br>
<br>

ar=recordcapture.micRecord()<br>
ar.start(seconds=30,filename=None,chunk=1024,channels=2,rate=44100,countdown=5,echo=True) <br>
#Note: All Parameters are optional<br>
seconds: total time to record the screen in seconds<br>
filename: any filename eg: abc.wav, if not provided, will take timestamp as default.<br>
chunk: chunk size<br>
channels: sound coming from points<br>
rate: sample rate<br>
countdown: countdown before start recording<br>
echo: to print the event messages<br>

<br>
<br>
<br>

ss=recordcapture.screenshot()<br>
ss.capture(countdown=5,filename=None,extension='png',echo=True)<br>
#Note: All Parameters are optional<br>
countdown: countdown before start recording<br>
filename: any filename eg: abc.png, if not provided, will take timestamp as default.<br>
extension: file extension<br>
echo: to print the event messages<br>


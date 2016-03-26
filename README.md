# tecedi-smartzap
Tecedi-SmartZap helps you control a HDMI switch with your Raspberry Pi so you can watch something interesting during TV ads. 

This is the Github repository associated with the Hackaday project https://hackaday.io/project/8944-tecedi-smartzap

Status
------
Work in progress! This is, at most, an alpha version. It can control a HDMI switch and play a video, but for the moment the logic for selecting which video to play has not been implemented

How to install?
--------------
This currently only works on Raspberry Pi. You need to install OSMC on a SD card as well as a few extra packages :
```
apt-get install gcc make python-dev python-pip
pip install RPi.GPIO
```
There is no install script yet, just copy the python files to a directory on the Raspberry pi and copy kodi-play-video-clip to /usr/local/bin/


How to run?
-----------
First you'll need the setup described in https://hackaday.io/project/8944-tecedi-smartzap.
You will also need to have a video with the following hardcoded path /videos/better-than-tv-ads.mp4 or you can edit this path in smartzap.py.
Then, login as root and launch smartzap.py. Your screen will temporarily switch to the RPI output, if it was not already selected, and then to your main STB ouput.

Press the '1' on your hdmi switch remote, your screen/TV should switch from the STB HDMI output to the RPI HDMI output and the RPI will start playing your video clip. At the end of the video clip, the HDMI switch will select the STB output and you'll be able to resume watching TV.

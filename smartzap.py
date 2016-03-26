#! /usr/bin/python
# -*- mode=python; encoding:utf-8 -*-

from hdmiswitchrpi import HdmiSwitchRpi
from kodiplayer import KodiPlayer
import time

VIDEO_FILE = '/videos/better-than-tv-ads.mp4'

def smartzap():
    """simple SmartZAp Poc"""
    print ("Entering SmartZap mode...")
    videoSwitch = HdmiSwitchRpi()
    videoSwitch.initHw()
    videoSwitch.switchBackToSTB()
    
    videoPlayer =  KodiPlayer()

    # we do polling, event_detect would be better but it doesn't work yet
    while True:
        if videoSwitch.isSmartZapOutputActive():
            videoPlayer.play(VIDEO_FILE)
            print('switching back to TV')
            videoSwitch.switchBackToSTB()
            time.sleep(1)
        else:
            time.sleep(1)
        
if __name__ == '__main__':
    smartzap()


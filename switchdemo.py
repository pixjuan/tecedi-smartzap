#! /usr/bin/python

import RPi.GPIO as GPIO
import time
from subprocess import call

class HdmiSwitch:
    """Handle control of a HDMI switch.
    HDMI port 1 : RPi
    HDMI port 2 : TV
    HDMI Led output pin connected : 1
    Button to use on the remote : 1
    
    The system should be started with HDMI port 2 active
    """

    # GPIO 17 PIN 11
    HDMI_STATUS_PIN = 11 

    # GPIO 18 PIN 12
    HDMI_SWITCH_PIN = 12

    # the time we have to wait after switching to the next HDMI port 
    PORT_CHANGE_DELAY = 1

    # the time we leave the GPIO signal low to simulate the button press
    GPIO_SWITCH_DELAY = 0.2

    # the number of ports in the switch
    NB_PORTS = 3


    def init(self):
        """initialize the GPIOs """
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.HDMI_STATUS_PIN, GPIO.IN)
        GPIO.setup(self.HDMI_SWITCH_PIN, GPIO.OUT)
        GPIO.output(self.HDMI_SWITCH_PIN, True)

    def nextHdmiInput(self):
        """
        send a GPIO pulse that mimic the 'change input' button press on the HDMI
        switch.
        """
        GPIO.output(self.HDMI_SWITCH_PIN, False)
        time.sleep(self.GPIO_SWITCH_DELAY)
        GPIO.output(self.HDMI_SWITCH_PIN, True)

    def switchBackToSmartZap(self):
        """ cycle through the HDMI ports until the RPi input is selected """
        v = GPIO.input(self.HDMI_STATUS_PIN)
        # if the switch is displaying our video output
        if v != True:
            for i in xrange(self.NB_PORTS):
                self.nextHdmiInput()
                time.sleep(self.PORT_CHANGE_DELAY)
                if GPIO.input(self.HDMI_STATUS_PIN):
                    break;

    def switchBackToTv(self):
        """ cycle through the HDMI ports until the STB input is selected """
        v = GPIO.input(self.HDMI_STATUS_PIN)
        # First we ensure the switch is displaying our video output
        if v == False:
            self.switchBackToSmartZap()
        # then we switch to the next one
        self.nextHdmiInput()

    def isSmartZapOutputActive(self):
        """ return true if the RPi HDMI input is active"""
        return GPIO.input(self.HDMI_STATUS_PIN)
        


# the command we'll use to play the video
VIDEO_PLAYER = '/usr/bin/omxplayer'
# the video file we are going to play
VIDEO_FILE = '/home/pi/video/better-than-tv-ads.mp4' 

def smartZap():
    """simple SmartZAp Poc"""
    print ("Entering SmartZap mode...")
    s = HdmiSwitch()
    s.init()
    s.switchBackToTv()
    
    # we do polling, event_detect would be better but it doesn't work yet
    while True:
        if s.isSmartZapOutputActive():
            call([VIDEO_PLAYER, VIDEO_FILE])
            print('switching back to TV')
            s.switchBackToTv()
            time.sleep(1)
        else:
            time.sleep(1)
        
if __name__ == '__main__':
    smartZap()


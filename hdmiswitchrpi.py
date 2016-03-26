#! /usr/bin/python
# -*- mode=python; encoding:utf-8 -*-

from hdmiswitch import HdmiSwitch
import RPi.GPIO as GPIO
import time

class HdmiSwitchRpi(HdmiSwitch):
    """Control a Generic HDMI switch with just 2 GPIOs.
    By "Generic HDMI Switch" we mean :
    - a switch which generally has 3 ports
    - input switching can be controlled by a button on the switch
    - there is a LED indicating which input is active
    
    The HdmiStatusPin GPIO which is connected to one of the input XXX active LED
    of the switch
    The HdmiSwitchPin GPIO which is connected to HDMI "next input" button

    HDMI port 1 : RPi HDMI
    HDMI port 2 : Set Top Box
    HDMI Led output pin connected : 1
    Button to use on the remote : 1
    
    The system should be started with HDMI port 2 active
    """

    def __init__(self):
        # the pin we will read to know if the player input is active
        self.hdmiStatusPin = 11 # GPIO 17 PIN 11

        # the pin we will write to to switch to the next HDMI input
        self.hdmiSwitchPin = 12 # GPIO 18 PIN 12

        # the amount of time we have to wait when switching to the next input
        self.switchDelay = 0.2

        # the number of input on the HDMI switch
        self.nbPorts = 3

    def initHw(self):
        """initialize the GPIOs"""
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.hdmiStatusPin, GPIO.IN)
        GPIO.setup(self.hdmiSwitchPin, GPIO.OUT)
        GPIO.output(self.hdmiSwitchPin, True)

    def nextHdmiInput(self):
        """
        send a GPIO pulse that mimic the 'change input' button press on the HDMI 
        switch.
        """
        GPIO.output(self.hdmiSwitchPin, False)
        time.sleep(self.switchDelay)
        GPIO.output(self.hdmiSwitchPin, True)

    def switchBackToPlayer(self):
        """cycle through the HDMI ports until the RPi input is selected"""
        v = GPIO.input(self.hdmiStatusPin)
        # if the switch is displaying our video output
        if v == False:
            for i in xrange(self.nbPorts):
                self.nextHdmiInput()
                time.sleep(1)
                if GPIO.input(self.hdmiStatusPin):
                    break;

    def switchBackToSTB(self):
        """cycle through the HDMI ports until the STB input is selected"""
        v = GPIO.input(self.hdmiStatusPin)
        # First we ensure the switch is displaying our video output
        if v == False:
            self.switchBackToPlayer()
        # then we switch to the next one
        self.nextHdmiInput()

    def isSmartZapOutputActive(self):
        """return True if the Rpi Output is active"""
        return GPIO.input(self.hdmiStatusPin)

    def selectInput(self, inputId):
        """Not implemented"""
        return False

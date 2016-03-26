# -*- mode=python; encoding:utf-8 -*-
class HdmiSwitch:
    """
    API to control a HDMI switch.
    This more specifically to switch between 2 video inputs, either a TV/STB one
    and a "player" one, that we control. Depending on the hardware imolementation, not all the 
    functions may be available
    """

    def initHw(self):
        """initialize the hardware, if any"""

    def nextHdmiInput(self):
        """
        mimic the 'change input' button press on the HDMI switch, 
        or more generally switch to the next HDMI Input ont the switch
        """

    def switchToPlayer(self):
        """switch to the Player input"""

    def switchToSTB(self):
        """switch to the STB input"""

    def isPlayerInputActive(self):
        """
        return True if the player input is active, False otherwise and None
        if the function is not implemented
        """
        return None

    def isTVInputActive(self):
        """
        return True if the player input is active, False otherwise and None
        if the function is not implemented
        """
        return None

    def getNumberOfPorts(self):
        """return the number of HDMI input ports"""
        return 0

    def selectInput(self, inputId):
        """select a specific input on the HDMI switch"""

    def PipCapable(self):
        """return True if the switch has a Picture-In-Picture mode"""
        return False

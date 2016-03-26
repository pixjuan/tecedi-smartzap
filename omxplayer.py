#! /usr/bin/python
# -*- mode=python; encoding:utf-8 -*-

from videoclipplayer import VideoClipPlayer
from subprocess import call

class OmxPlayer(VideoClipPlayer):
    """ Plays a video clip through Omxplayer """
    VIDEO_PLAYER = '/usr/bin/omxplayer'

    def play(self, file):
        """
        play a file.
        return True if the file can be played, False otherwise
        """
        retval = call([self.VIDEO_PLAYER, file])
        if retval == 0:
            return True
        else:
            return False


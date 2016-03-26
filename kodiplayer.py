#! /usr/bin/python
# -*- mode=python; encoding:utf-8 -*-

from videoclipplayer import VideoClipPlayer
from subprocess import call



class KodiPlayer(VideoClipPlayer):
    """ Plays a video clip through Kodi """

    # TODO : use JSON API or Kodi API instead of the kodi-play-clip script
    VIDEO_PLAYER = 'kodi-play-clip'

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

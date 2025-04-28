#!/usr/bin/python
# coding: utf-8
import sys
import config
from mylast import *
import subprocess
limit=10
#limit=10
def get_loved_tracks(limit=limit):
    return lastfm_network.get_user(lastfm_username).get_loved_tracks(limit)

def loved_tracks_to_json():
    tracks = get_loved_tracks()
    for x in tracks:
        try:
            tracks_dictionary[str(x.track.get_artist())].append((x.track.get_title()))
        except:
            tracks_dictionary[str(x.track.get_artist())]=[]
            tracks_dictionary[str(x.track.get_artist())].append((x.track.get_title()))
    return tracks_dictionary

def count_loved_tracks():
    return len(get_loved_tracks())

def print_loved_tracks():
    tracks = ''
    for i, track in enumerate(get_loved_tracks()):
        tracks += (str(track.track.get_artist())+" - "+str(track.track.get_title()))+'\n'
    return tracks[0:len(tracks)-2]

def generate_playlist(limit=limit):
    for i, track in enumerate(get_loved_tracks(limit)):
        tracks = subprocess.check_output(['mpc', 'search', 'title', str(track.track.get_title()), 'artist', str(track.track.get_artist())]).splitlines()
        if len(tracks) == 0:
            try:
                album_object = track.track.get_album()
            except:
                print(str(track.track.get_artist())+' '+str(track.track.get_title())+' not on last-fm', file=sys.stderr)
                album_object=False
            if album_object != None and album_object != False:
                tracks = subprocess.check_output(['mpc', 'search', 'title', str(track.track.get_title()), 'album', str(album_object.get_name())]).splitlines()
                if len(tracks) == 0:
                    print(str(track.track.get_artist())+' '+str(track.track.get_title())+' not found with album search', file=sys.stderr)
                elif len(tracks) >= 1:
                    print(config.music_basedir+str(tracks[0].decode('UTF-8')))
            elif album_object == None:
                print(str(track.track.get_artist())+' '+str(track.track.get_title())+' both methods failed', file=sys.stderr)
        elif len(tracks) >= 1:
            print(config.music_basedir+str(tracks[0].decode('UTF-8')))

if __name__ == '__main__' and sys.argv[1] == "generate_playlist" and sys.argv[2]:
    generate_playlist(int(sys.argv[2]))

if __name__ == '__main__' and sys.argv[1] == "print":
    print(print_loved_tracks())
